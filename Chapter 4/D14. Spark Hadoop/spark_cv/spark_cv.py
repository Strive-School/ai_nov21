from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext

from pyspark.ml.feature import VectorAssembler
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.classification import LogisticRegression


if __name__ == "__main__":

    conf = SparkConf(True)
    conf.set("spark.executor.memory","32g")
    conf.set("spark.executor.cores","4")

    sc = SparkContext(appName="MNIST_CLF", conf=conf)

    sql = SQLContext(sc)

    df = sql.read.format("com.databricks.spark.csv").options(header= True, inferSchema=True, sep=',').load("mnist_data/train.csv")

    features = df.schema.names[1:]
    vec  = VectorAssembler(inputCols=features, outputCol='features')
    df = vec.transform(df)

    df.select('label','features').show(5)

    train, test = df.randomSplit([0.8,0.2], 1)

    lr = LogisticRegression(maxIter=10,tol=1E-6, fitIntercept=True)

    model = lr.fit(train)

    result = model.transform(test)

    preds_lables = result.select('prediction', 'label')

    preds_lables.show(5)

    evaluator = MulticlassClassificationEvaluator()

    acc = evaluator.evaluate(preds_lables)

    print("LR acc:", acc)