#!/bin/bash

sudo systemctl daemon-reload &

echo -e "\n-------------------------------------- [$(date)]"
echo "- AI-Landingpage: SERVICE RESTARTING \n"

sudo systemctl restart ashgard_landingpage.service  
# sudo systemctl restart nginx

echo -e "\n-------------------------------------- [$(date)]"
echo "- AI-Landingpage: SERVICE RESTARTED \n\n"





