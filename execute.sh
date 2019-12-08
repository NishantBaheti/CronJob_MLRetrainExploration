
currDir="/home/nishant/Desktop/CronJob_MLRetrainExploration"
dataFileName="${currDir}/iris.csv"
echo ${dataFileName}
if [ -e ${dataFileName} ]
then
    python3 ${currDir}/trainMachineLearningModel.py
    echo "model saved"
else
    echo "some problem with input file"
fi
