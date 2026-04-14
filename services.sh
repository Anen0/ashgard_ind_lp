#!/bin/bash

sudo systemctl daemon-reload &

echo -e "\n-------------------------------------- [$(date)]"
echo "- AI-Landingpage: SERVICE RESTARTING"

sudo systemctl restart ashgard_landingpage.service  
# sudo systemctl restart nginx

echo "- AI-Landingpage: SERVICE RESTARTED"





