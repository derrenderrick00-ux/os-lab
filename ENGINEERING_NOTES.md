# OS Lab v3.0 engineering build — Phase 0–6

## Scope and limits

This release preserves all v2.0.1 files and adds `engineering.js` with a new **Engineering Lab** tab. It does not replace the original lesson or troubleshooting implementations. The 60 existing scenarios are selectable in the new lab, but most use **category-level fault models** rather than individually faithful OS-specific implementations. This is not full OS virtualization. Commands implement a finite educational subset, not a real Bash/CMD/PowerShell parser. The `fix` command is a clearly labeled teaching shortcut for faults not supported by native-style repair commands.

## Phase coverage

- Phase 0: preserved baseline and separate v3 storage key; regression and smoke-test infrastructure.
- Phase 1: shell modes, command dispatch, error handling, permissions, history and documented subset of simulated CLI commands.
- Phase 2: shared state for virtual processes, RAM, storage, files, network, services, boot, devices and logs inside the Engineering Lab.
- Phase 3: 60 selectable legacy cases mapped to state-driven category fault templates; reset, repair and verify. Distinct per-case root causes remain future work.
- Phase 4: guided, independent and exam modes; evidence-based scoring and attempt history. Diagnosis grading recognizes keywords, not semantic correctness; assessment is for self-study, not certification.
- Phase 5: machine status and assessment metrics. Detailed packet timelines and cross-subsystem charts are not implemented in this build.
- Phase 6: syntax and headless-browser smoke checks, offline ZIP, documentation and baseline compatibility. Windows real-browser acceptance remains for user verification.

## Safety and compatibility

- No `eval`, shell process, OS command execution, network requests, or external packages.
- Virtual commands mutate JavaScript objects only.
- v2.0.1 legacy progress uses its original key; Engineering Lab assessments use `oslab-v3-engineering-v1`.
- Export legacy progress separately using Progress, and v3 assessments using Engineering Lab.
- Machine state is intentionally ephemeral; assessment history persists in localStorage.

## CLI examples

```
help
ip addr
ip route
resolvectl status
resolvectl query example.com
login admin
resolvectl dns eth0 1.1.1.1
verify
diagnosis DNS server misconfiguration
```

For category-level cases not yet supported by a native-style repair command, use `login admin` then `fix network`, `fix storage`, `fix memory`, `fix boot`, `fix security`, or `fix service`.

## Known gaps to prioritize

1. Individually model all 60 faults with correct evidence and unique repairs.
2. Implement a true tokenization/quoting grammar for each shell and more accurate command semantics.
3. Improve semantic diagnosis assessment and add explicit verification evidence requirements.
4. Add process/memory/filesystem/network timelines and richer visualizations.
5. Add full end-to-end browser tests for both Ubuntu and Windows.
