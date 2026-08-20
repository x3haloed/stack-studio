# vm-stack Windows field trial

## Evidence classification

This is a repository-guided field trial from a sustained user-agent engagement.
It is independent anchor evidence for Stack Studio's operating model, but it is
not a fresh-agent run and must not be compared numerically with the fixed
scenario runs.

## Starting outcome

Use Stack Studio to improve an existing VM skill stack far enough to create and
manage a Windows VM that could validate Windows-specific stack tooling. Preserve
the target's existing VM-management authority and obtain live Windows evidence.

## Observed journey

The work proceeded through repeated implementation-and-observation cycles:

1. The agent inspected the existing stack and preserved its manager script as
   the sole authority for VM disk and runtime operations.
2. Missed UEFI optical boot, Windows Setup failure, OpenSSH behavior, SCP path
   semantics, writable firmware state, OOBE automation, Sysprep ordering, and
   activation timing each contradicted an earlier working assumption.
3. Each discrepancy was resolved with the smallest practical probe: managed
   console evidence, Windows logs, official documentation, fresh installation,
   or a clean thin clone.
4. Consequential user evidence changed two target invariants: routine
   administration inside purpose-created managed guests should not be handed
   back to the user, and purpose-complete disposable VMs should be released
   after evidence is preserved.
5. The resulting target stack installed Windows unattended, provisioned
   VirtIO and OpenSSH offline, sealed a generalized reusable base, created
   identity-distinct thin clones, reported activation truthfully, and routed
   lifecycle operations through one manager.

## Prediction error relevant to Stack Studio

The work initially treated successful behavioral validation as the practical
completion boundary. Two successful validation clones remained allocated after
their evidence had already been captured, consuming substantial disk space.
The user identified that the resources had served their purpose and should have
been removed.

The target stack was then revised so sealed-base clones require a purpose and
an observable release condition, default to disposable, and can be released
through a guarded manager transition. The completed clones were removed and the
single reusable base was retained and compressed.

## Durable evidence

- A clean Windows installation reached real SSH readiness without manual OOBE.
- Two clean clones had different Windows hostnames and different SSH host-key
  hashes.
- Activation was reported separately from technical readiness and retried only
  after networking was usable.
- The disposable clone directory was reduced from approximately 24.5 GB to
  effectively empty after the validation purpose was satisfied.
- The single reusable base remained as the minimum durable infrastructure for
  avoiding another full Windows installation.

## Stack Studio conclusion

The single-controller adaptive loop worked: repository authority, human
judgment, prediction-error handling, runtime evidence, and domain-specific
metabolism remained distinct. The missing general guidance was purpose-bound
resource disposition. This property should be added to Stack Studio's
controller and tested in the existing-stack scenario without creating another
generic lifecycle skill.
