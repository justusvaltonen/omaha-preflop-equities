# Project Workflow and Security Considerations for Omaha Preflop Equities

This document details the overall workflow for the Omaha Preflop Equities distributed calculation project and consolidates key security considerations to ensure data integrity, participant privacy, and robust operation.

## Overall Project Workflow

The project operates on a distributed computing model where individual participants contribute computational resources to solve complex Omaha preflop equity calculations. The workflow is designed to be transparent, verifiable, and secure.

### 1. Task Distribution

Calculation tasks (e.g., specific hand match-ups) are defined and made available to participants. The mechanism for task distribution will be detailed in a separate document, but it will ensure that tasks are unique and trackable.

### 2. Local Calculation and Data Generation

Participants run calculation software on their local machines. This software performs the assigned equity calculations. The results of these calculations are initially stored in the browser's local storage and then automatically transferred to a designated local folder on the participant's computer.

### 3. Secure Data Ingestion

As detailed in the [Secure Data Ingestion Method](data_ingestion_method.md) document, a local script on the participant's machine detects new result files. It then obtains a temporary, secure upload token and uses it to upload the results to one of several distributed secure storage locations. This process ensures that no plain-text credentials are ever exposed.

### 4. Data Aggregation and Validation

Periodically, a central automated process (e.g., `scripts/aggregate_validate.py`) retrieves new raw data from the secure storage locations. This process performs the following:

*   **Checksum Verification**: Ensures data integrity during transit.
*   **Duplicate Task Grouping**: Groups submissions for the same calculation task.
*   **Consistency Check**: Compares results from multiple submissions for the same task. As designed, approximately 20% of calculations may initially be inconsistent, requiring re-calculation. Inconsistencies trigger alerts for investigation.
*   **Validation**: If multiple submissions for a task are consistent, the result is marked as validated.
*   **Aggregation**: Validated results are aggregated into a master equity map (e.g., `data/aggregated/omaha_preflop_equities_map.json`).

### 5. Public Repository Synchronization

Validated and aggregated data, along with scripts and documentation, are regularly committed to the public GitHub repository. This provides transparency and a central, version-controlled record of the project's progress and results.

## Security Considerations

Security is paramount in this distributed project, especially given the involvement of multiple participants and the public nature of the repository. The following measures are in place:

*   **Credential Handling**: Absolutely no plain-text credentials (e.g., GitHub tokens, cloud storage keys) are stored or transmitted by participants. All interactions requiring authentication utilize secure, short-lived tokens or OAuth flows.
*   **Data Storage**: Raw calculation results are stored in distributed, secure, off-GitHub locations. Only processed, validated, and non-sensitive aggregated data is committed to the public GitHub repository.
*   **Data Integrity**: Checksums and cryptographic hashes are used to verify the integrity of data during transfer and storage, ensuring that results have not been tampered with.
*   **Access Control**: Access to secure storage locations and authentication services is strictly controlled and monitored. The responsibility for managing these secure locations rotates among trusted project members.
*   **Public Transparency vs. Confidentiality**: While the project aims for transparency, sensitive operational details (e.g., specific cloud storage endpoints, internal authentication service URLs) are kept separate from the public repository.
*   **Vulnerability Management**: Regular reviews of scripts and infrastructure will be conducted to identify and mitigate potential security vulnerabilities.
*   **Designed Inconsistency**: The planned 20% inconsistency rate acts as a built-in security and validation mechanism, forcing cross-verification and early detection of potential errors or malicious data injections.

This comprehensive approach to workflow and security aims to build a trustworthy and efficient distributed computing environment for the Omaha Preflop Equities project.
