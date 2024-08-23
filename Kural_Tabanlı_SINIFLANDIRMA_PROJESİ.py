import pandas as pd

df = pd.read_csv('Datasets/persona.csv')

df.info()
df.head()
df.tail()
df.describe().T
print(df.shape)
print(df.columns)
print(df.index)
df.isnull().values.any()


#Kaç adet unique source vardır? Frekansları nelerdir?

df['SOURCE'].value_counts()
df['SOURCE'].unique()

#Kaç Adet unique PRICE vardır?

df.PRICE.nunique()


# Hangi PRICEDEN kaçar tane satış gerçekleşmiş

df.PRICE.value_counts()



# Hangi ülkeden kaçar tane satış olmuş?


df.COUNTRY.value_counts()

 # ülkelere göre satışlardan toplam ne kadar kazanılmış.


df.groupby('COUNTRY').agg({'PRICE': 'sum'})
# df.groupby('COUNTRY')['PRICE'].sum()  yukarıdaki ile aynı işi yapar.

df.SOURCE.value_counts()



# ÜLKELERE GÖRE PRICE ORTALAMASI NEDİR

df.groupby('COUNTRY').agg({'PRICE': 'mean'})

# SOURCE'lara göre PRICE  ortalamaları nedir?

df.groupby('SOURCE').agg({'PRICE': 'mean'})


# COUNTRY- SOURCE GÖRE PRICE ORTALAMALARI

df.groupby(['COUNTRY','SOURCE']).agg({'PRICE': 'mean'})


######################################################
# GÖREV2:COUNTRY,SOURCE,SEX,AGE, kırılımında ortalama kazançlar nelerdir
######################################################


# df.groupby(['COUNTRY','SOURCE','SEX','AGE']).agg({})





#GÖREV3: çıktıyı PRICE'a göre sıralayınız


agg_df.sort_values('PRICE', ascending = False)
len(agg_df.columns)






#GÖREV4:

agg_df.reset_index()





# AGE değişkenini kategorik değişkene çeviriniz ve agg_df'e ekleyiniz.

#Aralıkları ikna edici olacağı düşündüğümüz şekilde oluşturunuz

#AGE değişkeninin nerelerden bölüneceği belirtelim:

my_bins = [0,18,23,30,40, agg_df['AGE'].max()]

# Bölünecek noktalara karşılık isimlendirmenin ne olacağını belirleyelim

my_labels = ['0_18', '19_23','24_30','31_40','41_' + str(agg_df['AGE'].max())]
my_labels = ['0_18', '19_23','24_30','31_40',f'41_{agg_df["AGE"].max()}']
print(my_labels)

# AGE'i bölelim:

pd.cut(agg_df['AGE'], bins=my_bins, labels=my_labels)


agg_df['AGE_CAT'] = pd.cut(agg_df['AGE'], bins=my_bins, labels=my_labels)
agg_df.head()






#Yeni seviye tabanlı müşterileri (persona) tanımlayınız ve veri setine değişken olarak ekleyiniz.
# Yeni eklenecek değişkenin adı: customers_level_based
# Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek customers_level_based değişkenini oluşturmanız gerekmektedir.

agg_df.drop(['AGE','PRICE'], axis = 1).values

liste = ['A','B','C']
'-'.join(Liste)

agg_df["CUSTOMER_LEVEL_BASED"] = ['_'.join(i).UPPER() for i in agg_df.drop(['AGE', 'PRICE'], axis = 1).values]
print(agg_df)
# Gereksiz değişkenleri çıkaralım


agg_df.head()


agg_df = agg_df.drop[['CUSTOMERS_LEVEL_BASED', 'PRICE']]


agg_df = agg_df.groupby('CUSTOMERS_LEVEL_BASED')['PRICE'].mean().reset_index()

#Yeni müşterileri (Örnek: USA_ANDROID_MALE_0_18) PRICE’a göre 4 segmente ayırınız.
#• Segmentleri SEGMENT isimlendirmesi ile değişken olarak agg_df’e ekleyiniz.
#• Segmentleri betimleyiniz (Segmentlere göre group by yapıp price mean, max, sum’larını alınız).


[23,27,34,34,35,39,41,48]

agg_df['SEGMENT'] = pd.qcut(agg_df.PRICE, q=4, labels=['D','C','B','A'])
agg_df.head()
agg_df.groupby('SEGMENT').agg({'PRICE': ['mean', 'sum','min','max']})


#• 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?


new_user = 'TUR_ANDROID_FEMALE_31_40'
agg_df[agg_df['CUSTOMERS_LEVEL_BASED'] == new_user]


#• 35 yaşında IOS kullanan bir Fransız kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?

new_user = 'FRA_ANDROID_FEMALE_31_40'
agg_df[agg_df['CUSTOMERS_LEVEL_BASED'] == new_user]
agg_df[agg_df['CUSTOMERS_LEVEL_BASED'] == 'BRA_ANDROID_FEMALE_0_18']
