# Omaha Preflop Equities - Distributed Calculation Project

A collaborative project for calculating Omaha poker preflop equities through distributed computing. This project enables multiple participants to contribute computational power to solve complex equity calculations that would take weeks on a single machine.

## Project Overview

This project aims to calculate comprehensive Omaha preflop equities with maximum accuracy. The calculations are distributed across multiple devices/users, with results automatically synchronized through secure channels.

### Key Features

- **Distributed Computing**: Calculations are split across multiple participants
- **Automatic Synchronization**: Results are automatically downloaded and synchronized
- **Data Validation**: Built-in validation to detect calculation errors (approximately 20% expected error rate by design)
- **Public Transparency**: All progress and results are publicly visible
- **Secure Data Handling**: No plain text credentials, secure authentication methods

### Project Structure

```
omaha-preflop-equities/
├── data/                    # Calculation results and intermediate data
│   ├── raw/                # Raw calculation outputs from participants
│   ├── validated/          # Validated and cross-checked results
│   └── aggregated/         # Final aggregated equity maps
├── scripts/                # Data processing and validation scripts
├── docs/                   # Project documentation
├── config/                 # Configuration files (no credentials!)
└── tools/                  # Utilities for participants
```

## Getting Started

### For Participants

1. Clone this repository
2. Set up your local environment (instructions in `docs/setup.md`)
3. Configure your data sync settings (see `docs/sync-setup.md`)
4. Start contributing calculations!

### Data Flow

1. **Calculation**: Each participant runs calculations on their assigned tasks
2. **Local Storage**: Results are saved to browser local storage, then copied to local folders
3. **Upload**: Participants upload their results to designated secure storage
4. **Validation**: Multiple instances calculate the same tasks for cross-validation
5. **Aggregation**: Validated results are combined into the master equity map

## Security Considerations

- **No Plain Text Credentials**: All authentication uses secure token-based methods
- **Public Repository**: All code and non-sensitive data are publicly visible
- **Secure Storage**: Calculation results are stored in multiple secure locations
- **Rotation System**: Responsibility for data parsing rotates among secure storage locations

## Current Status

- **Phase 1**: Initial setup and infrastructure (< 100MB data expected)
- **Estimated Completion**: Significantly longer than initial AI estimates suggested
- **Error Rate**: ~20% of calculations expected to require recalculation (by design)

## Contributing

See `docs/CONTRIBUTING.md` for detailed contribution guidelines.

## License

This project is open source. See `LICENSE` for details.
