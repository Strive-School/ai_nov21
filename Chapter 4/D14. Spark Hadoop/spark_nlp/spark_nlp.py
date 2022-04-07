import pyspark as ps
from pyspark.sql import SQLContext
from pyspark.ml.feature import CountVectorizer, Tokenizer, HashingTF, IDF, StringIndexer
from pyspark.ml.classification import NaiveBayes
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml import Pipeline

sc = ps.SparkContext.getOrCreate()
sql = SQLContext(sc)

train = sql.read.format('com.databricks.spark.csv').options(header=False, inferSchema=True, sep=';' ).load('sentiment_data/train.csv')
test = sql.read.format('com.databricks.spark.csv').options(header=False, inferSchema=True, sep=';' ).load('sentiment_data/test.csv')

train = train.withColumnRenamed('_c0','description').withColumnRenamed('_c1','target')
test = test.withColumnRenamed('_c0','description').withColumnRenamed('_c1','target')

print(train.count())
train.dropna()
test.dropna()


ordinal_enc = StringIndexer(inputCol='target', outputCol='label')
tokenizer = Tokenizer(inputCol='description', outputCol='tokens')
tf = HashingTF(inputCol='tokens', outputCol='tf_tokens', numFeatures=2**16)
idf = IDF(inputCol='tf_tokens', outputCol='features', minDocFreq = 3 )


pipe = Pipeline(stages= [ordinal_enc,tokenizer,tf,idf] )

pipe = pipe.fit(train)
train = pipe.transform(train)
train.select('tokens','tf_tokens', 'features').show(10)

test = pipe.transform(test)

nb = NaiveBayes(smoothing=1, modelType="multinomial")


model = nb.fit(train)

results = model.transform(test)

criterion = MulticlassClassificationEvaluator()

acc = criterion.evaluate(results)

print(acc)
