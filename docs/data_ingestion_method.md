
NOT INFILTRATING OTHERS MACHINES. I WILL DO A TOTAL REMAKE OF ALL THIS SCRIPTING THING

# Secure Data Ingestion Method for Omaha Preflop Equities Project

This document outlines a secure and robust method for ingesting calculation results from distributed participant machines into the central project data stores. Given the distributed nature of the calculations and the need for data integrity and security, especially regarding credentials, a multi-tiered approach is proposed.

## Principles of Secure Data Ingestion

1.  **No Plain-Text Credentials**: Participants will not handle or transmit plain-text GitHub credentials. All authentication will rely on secure, short-lived tokens or other secure authentication flows.
2.  **Automated & Localized Collection**: Calculation results are initially collected automatically from browser local storage to a local folder on the participant's machine. This ensures participants retain a copy of their work and provides a local buffer before synchronization.
3.  **Secure Upload Mechanism**: A secure, token-based upload mechanism will be used to transfer data from participant machines to designated secure storage locations. This could involve using pre-signed URLs for cloud storage or a dedicated API endpoint with OAuth/JWT authentication.
4.  **Distributed Secure Storage**: Data will be stored in multiple secure, off-GitHub locations, managed by trusted project members. These locations will act as the primary storage for raw calculation data before it is processed and validated.
5.  **Data Integrity and Validation**: Each data submission will be accompanied by a checksum or hash to ensure data integrity during transit. The validation process will involve comparing results from multiple participants for the same calculation task.

## Proposed Workflow

1.  **Participant-Side Script**: A script will be provided to participants that runs on their local machine. This script will:
    *   Monitor a designated local folder for new calculation result files.
    *   When a new file is detected, it will request a temporary upload token from a central authentication service.
    *   Use the token to upload the file to one of the designated secure storage locations.

2.  **Authentication Service**: A simple, secure authentication service will be created. This service will be responsible for:
    *   Authenticating participants (e.g., via their GitHub account using an OAuth flow).
    *   Issuing short-lived, single-use upload tokens (e.g., pre-signed URLs for a cloud storage bucket).

3.  **Secure Storage**: The secure storage locations (e.g., private cloud storage buckets) will be configured to only accept uploads with valid, unexpired tokens. This prevents unauthorized data submission.

4.  **Data Processing and Aggregation**: A separate, automated process will periodically fetch new data from the secure storage locations, perform validation and aggregation, and then commit the validated results to the public GitHub repository.

This approach ensures that participant credentials are never exposed, and the data ingestion process is secure, automated, and scalable.
