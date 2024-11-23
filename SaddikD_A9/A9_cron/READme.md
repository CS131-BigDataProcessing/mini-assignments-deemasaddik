# Automated System Maintenance Tasks

This README describes three Cron jobs set up for automated system maintenance: daily file cleanup, weekly system backup, and daily disk usage reporting.

## 1. Daily File Cleanup

### Description
This job removes all files from a specified temporary directory on a daily basis.

### Cron Schedule
0 2 * * * rm /mnt/scratch/FA24_CS131_Jessica/dsaddikfa24/temp/*

- Runs every day at 2:00 AM
- Deletes all files in the `/mnt/scratch/FA24_CS131_Jessica/dsaddikfa24/temp/` directory

## 2. Weekly System Backup

### Description
This job creates a tar archive of a specified directory on a weekly basis.

### Cron Schedule
0 3 * * 7 tar -cf archive.tar /mnt/scratch/FA24_CS131_Jessica/dsaddikfa24/backups

- Runs every Sunday at 3:00 AM
- Creates a tar archive named `archive.tar` of the `/mnt/scratch/FA24_CS131_Jessica/dsaddikfa24/backups` directory

## 3. Daily Disk Usage Report

### Description
This job sends a daily email report of disk usage.

### Cron Schedule
30 8 * * * df -h | mail -s "Disk Usage Report" deema.saddik@gmail.com

- Runs every day at 8:30 AM
- Generates a disk usage report using `df -h` command
- Emails the report to deema.saddik@gmail.com with the subject "Disk Usage Report"

## Setup Instructions

1. Open the crontab file for editing:
   crontab -e

2. Add the above Cron job lines to the file.

3. Save and exit the editor.

## Notes

- Ensure that the specified directories exist and have appropriate permissions.
- For the email job, make sure the system is configured to send emails.
- Adjust the timing and paths as needed for your specific system configuration.
