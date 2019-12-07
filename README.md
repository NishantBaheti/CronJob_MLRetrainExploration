Cron Job for ML Model Retraining :

To Schedule a cron Job << Steps>>
--------------------------------------------
For Ubuntu 16.04 -

1. Install cron -
	
	$apt-get update && $apt-get upgrade

	// Check if cron package is installed:

	// To check if cron is installed, run the following command –
	$dpkg -l cron 

	// If cron is not installed, install the cron package on Ubuntu:
	// One can Install the cron package with package Manager using the following command-

	$apt-get install cron

	// Verify if cron service is running:
	// To check whether the cron service is running on the system, we can use the following command-

	$systemctl status cron

2. add a cronjob - 
	
	$crontab -e
	
	// insert the following entry for schedule job for every hour retraining
	
	0 * * * * /path/to/bashScript/execute.sh

	save
	// ESC :wq

3. check list - 
	
	$crontab -l

4. check logs - 
	$systemctl status cron

