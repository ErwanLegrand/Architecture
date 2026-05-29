# Write-ahead audit

Commit the invocation record before executing the action it authorizes, parallel to database write-ahead logging. A crash between record and action leaves no unrecorded state changes.
