from flask import Flask # type: ignore
from flask import request # type: ignore
from flask import jsonify, make_response, redirect, url_for # type: ignore
from flask import render_template # type: ignore

app = Flask(__name__)

@app.route("/")
def sa():
  return 'Sa'

# temel
@app.route("/anasayfa")
def anasayfa():
  return 'Ana Sayfa'


@app.route("/urunler/<product>")
def urunprofil(product):
  return f'ürünler: {product}'

# tip dönüşümleri
@app.route("/urun/<int:urun_id>")
def urun_detay(urun_id):
  return f"Ürünün Id'si: {urun_id} (tip:{type(urun_id)})"


@app.route('/fiyat/<float:tutar>')
def fiyat_goster(tutar):
  return f'Fiyat: {tutar}'

@app.route('/dosyalar/<path:dosya_yolu>')
def dosya_goster(dosya_yolu):
  return f'Dosya Yolu: {dosya_yolu}'

@app.route('/giris', methods=['GET', 'POST'])
def giris():
  if request.method == 'POST':
    return 'POST isteği alındı'
  else:
    return 'Giris formundasınız'
  
# sadece POST kabul etsin istiyorsak
@app.route('/api/veri', methods=['POST'])
def veri_al():
  return 'sadece POST kabul edilir'

# @app.route('/test/') # sonuna / koymazsak 404 hatası verir

# HTTP Talep ve cevapları
# request.form.get() ile form verilerini alabiliriz. Form verileri, HTML formu aracılığıyla gönderilen verilerdir. Bu veriler, genellikle kullanıcı tarafından doldurulan input alanlarından gelir. Örneğin, bir kullanıcı adını ve soyadını içeren bir formunuz varsa, bu verileri request.form.get() ile alabilirsiniz.
#request.form.get() ile verileri çekeriz
#ops1 --- ad=str()
@app.route('/form', methods = ['GET', 'POST'])
def form():
  ad=request.form.get('ad')
  soyad=request.form.get('soyad')
  return f"Merhaba {ad} {soyad}"
  # ops1 ---request.form.[ad]

# ?/q=flask&sayfa2 --- # q query'den gelir q=flask ve sayfa=2 query parametreleridir. Bu parametreler, URL'nin ? işaretinden sonra gelir ve genellikle anahtar-değer çiftleri şeklinde düzenlenir. Örneğin, q=flask ifadesi, q adlı bir parametrenin değerinin flask olduğunu belirtir. Benzer şekilde, sayfa=2 ifadesi, sayfa adlı bir parametrenin değerinin 2 olduğunu gösterir. Bu parametreler, web uygulamalarında genellikle arama sorguları veya sayfalama gibi durumlarda kullanılır.

@app.route('/form_2', methods = ['GET', 'POST'])
def form_2():
  ad=request.form.get('ad')
  soyad=request.form.get('soyad')
  return f"Merhaba {ad} {soyad}"
  # query parametreleri yani URL'deki key value değerleri
  sayfa = request.args.get('sayfa',1,type=int) # sayfa parametresini alır, eğer yoksa 1 varsayılan değeri kullanır ve int tipine dönüştürür
  # cookiler
  denemecooki = request.cookies.get('herhangibirçerez')
  # headers
  deneme = request.headers.get('Deneme')
  # JSON verisi için
  if request.is_json:
    data = request.get_json()
    return 'Json verisi hazir'
  

# JSON Cevabı için
@app.route('/api/kullanicilar')
def kullanicilar_api():
  kullanicilar = [
    {'id': 1, 'ad': 'Ali'},
    {'id': 2, 'ad': 'Ayşe'},
    {'id': 3, 'ad': 'Mehmet'}
  ]
  return jsonify(kullanicilar)

# özel statülü kodlar
@app.route('/hata')
def hata():
  return 'Bir hata oluştu', 404

# cookileri setleme
@app.route('/cookie-set')
def cookie_set():
  resp = make_response('Cooki ayari cekildi')
  resp.set_cookie('kullanici', 'Ali')
  return resp

# routing yönlendirme
@app.route('/eski-sayfa')
def eski_sayfa():
  return redirect(url_for('anasayfa'))

# jinja2 Template -> html sayfalarını dinamik olarak oluşturmak için kullanılır. Jinja2, Python tabanlı bir şablon motorudur ve Flask ile birlikte kullanılır. Jinja2, HTML dosyalarına Python kodu ekleyerek dinamik içerik oluşturmanıza olanak tanır. Örneğin, bir kullanıcı listesi oluşturmak istiyorsanız, Jinja2 kullanarak bu listeyi HTML içinde döngü ile oluşturabilirsiniz. Ayrıca, Jinja2 değişkenler, koşullar ve filtreler gibi özellikler sunar, böylece HTML içeriğinizi daha esnek ve dinamik hale getirebilirsiniz.

@app.route('/kullanici')
def index():
    kullanici_adi = 'Batuhan'
    return render_template('index.html', kullanici_adi=kullanici_adi)


if __name__ == "__main__":
  app.run(debug=True)