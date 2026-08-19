#!/usr/bin/env bash
# List SKILL.md files with their frontmatter name and description.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
DEFAULT_ROOT="$(cd "$SCRIPT_DIR/../../.." 2>/dev/null && pwd -P || pwd -P)"

if [ "${1:-}" = "-h" ] || [ "${1:-}" = "--help" ]; then
    echo "usage: $(basename "$0") [-h] [root]"
    echo ""
    echo "Print file path, name, and description for all SKILL.md files."
    echo ""
    echo "positional arguments:"
    echo "  root        Directory to scan recursively. Defaults to the repository root."
    echo ""
    echo "options:"
    echo "  -h, --help  show this help message and exit"
    exit 0
fi

if [ "$#" -gt 1 ]; then
    echo "usage: $(basename "$0") [-h] [root]" >&2
    exit 2
fi

RAW_ROOT="${1:-$DEFAULT_ROOT}"
# Expand leading tilde if present
if [[ "$RAW_ROOT" == ~* ]]; then
    RAW_ROOT="${RAW_ROOT/#\~/$HOME}"
fi

if [ ! -d "$RAW_ROOT" ]; then
    echo "error: root is not a directory: $RAW_ROOT" >&2
    exit 2
fi

ROOT="$(cd "$RAW_ROOT" && pwd -P)"

trim() {
    local var="$*"
    # Remove leading whitespace
    var="${var#"${var%%[![:space:]]*}"}"
    # Remove trailing whitespace
    var="${var%"${var##*[![:space:]]}"}"
    printf '%s' "$var"
}

unquote() {
    local val="$1"
    val="$(trim "$val")"
    local len="${#val}"
    if [ "$len" -ge 2 ]; then
        local first="${val:0:1}"
        local last="${val:$((len - 1)):1}"
        if [ "$first" = "$last" ]; then
            if [ "$first" = '"' ] || [ "$first" = "'" ]; then
                val="${val:1:$((len - 2))}"
            fi
        fi
    fi
    printf '%s' "$val"
}

one_line() {
    local val="$1"
    local restore_glob=0
    case "$-" in
        *f*) restore_glob=0 ;;
        *) restore_glob=1 ;;
    esac
    set -f
    local IFS=$' \t\n'
    # shellcheck disable=SC2086
    set -- $val
    local res="$*"
    if [ "$restore_glob" -eq 1 ]; then
        set +f
    fi
    printf '%s' "$res"
}

read_frontmatter() {
    local file="$1"
    local -a fm_lines=()
    local in_fm=0
    local first_line=1

    while IFS= read -r line || [ -n "$line" ]; do
        line="${line%$'\r'}"
        local trimmed
        trimmed="$(trim "$line")"

        if [ "$first_line" -eq 1 ]; then
            first_line=0
            if [ "$trimmed" = "---" ]; then
                in_fm=1
                continue
            else
                break
            fi
        fi

        if [ "$in_fm" -eq 1 ]; then
            if [ "$trimmed" = "---" ]; then
                break
            fi
            fm_lines+=("$line")
        fi
    done < "$file"

    local num_lines="${#fm_lines[@]}"
    local idx=0
    local name=""
    local description=""

    while [ "$idx" -lt "$num_lines" ]; do
        local line="${fm_lines[$idx]}"

        # Skip if no colon or starts with whitespace
        if [[ "$line" != *:* ]] || [[ "$line" =~ ^[[:space:]] ]]; then
            idx=$((idx + 1))
            continue
        fi

        local key="${line%%:*}"
        local value="${line#*:}"

        key="$(trim "$key")"

        if [ "$key" = "name" ] || [ "$key" = "description" ]; then
            local val_trimmed
            val_trimmed="$(trim "$value")"

            case "$val_trimmed" in
                "|"|"|-"|"|+"|">"|">-"|">+")
                    local block_text=""
                    idx=$((idx + 1))
                    while [ "$idx" -lt "$num_lines" ]; do
                        local next_line="${fm_lines[$idx]}"
                        local next_trimmed
                        next_trimmed="$(trim "$next_line")"

                        if [[ "$next_line" =~ ^[[:space:]] ]] || [ -z "$next_trimmed" ]; then
                            if [ -n "$block_text" ]; then
                                block_text="${block_text}"$'\n'"${next_trimmed}"
                            else
                                block_text="${next_trimmed}"
                            fi
                            idx=$((idx + 1))
                        else
                            break
                        fi
                    done
                    local block_val
                    block_val="$(one_line "$block_text")"
                    if [ "$key" = "name" ]; then
                        name="$block_val"
                    else
                        description="$block_val"
                    fi
                    continue
                    ;;
                *)
                    local unquoted
                    unquoted="$(unquote "$val_trimmed")"
                    local processed_val
                    processed_val="$(one_line "$unquoted")"
                    if [ "$key" = "name" ]; then
                        name="$processed_val"
                    else
                        description="$processed_val"
                    fi
                    ;;
            esac
        fi
        idx=$((idx + 1))
    done

    PARSED_NAME="$name"
    PARSED_DESCRIPTION="$description"
}

printf '%s\t%s\t%s\n' "path" "name" "description"

find "$ROOT" \
    \( -name .git -o -name node_modules -o -name .venv -o -name venv -o -name __pycache__ \) -prune \
    -o -type f -name "SKILL.md" -print0 | LC_ALL=C sort -z | while IFS= read -r -d '' file; do
        read_frontmatter "$file"
        
        if [ "$ROOT" = "/" ]; then
            rel_path="${file#/}"
        else
            rel_path="${file#"$ROOT/"}"
        fi
        
        printf '%s\t%s\t%s\n' "$rel_path" "$PARSED_NAME" "$PARSED_DESCRIPTION"
    done
