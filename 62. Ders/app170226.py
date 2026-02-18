from flask_wtf import FlaskForm  # type: ignore
from wtforms import StringField, SubmitField, PasswordField  # type: ignore
from wtforms.validators import DataRequired, Email, Length, EqualTo  # type: ignore
from flask import Flask  # type: ignore
from flask import request  # type: ignore
from flask import jsonify, make_response, redirect, url_for  # type: ignore
from flask import render_template  # type: ignore

app = Flask(__name__)


class GirisFormu(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    sifre = PasswordField('Şifre', validators=[DataRequired(), Length(min=8)])
    sifre_tekrar = PasswordField('Şifre Tekrar', validators=[
                                 DataRequired(), EqualTo('sifre')])
    submit = SubmitField('Giriş Yap')

# IntegerField: Tam sayı için
# FloatField: Ondalıklı sayı için
# BooleanField: Doğru/yanlış değeri için
# SelectField: Seçim listesi için
# TextAreaField: Çok satırlı metin girişi için
# FileField: Dosya yükleme için
# DateField: Tarih verisi almak için
# URL() validator: URL doğrulaması için
# Diğer validatorlar
# NumberRange(min=a, max=b) validator: Sayısal değerlerin belirli bir aralıkta olup olmadığını kontrol etmek için
# EqualTo('field_name') validator: İki alanın eşit olup olmadığını kontrol etmek için (örneğin, şifre ve şifre doğrulama alanları) - Burada başka bir field ile eş olma zorunluluğu istiyor isek, şifre-kullanici_adi gibi


# SECRET_KEY ayarı
app.config['SECRET_KEY'] = 'gizli_anahtar'  # Güvenli bir anahtar kullanın


@app.route('/girisflask', methods=['GET', 'POST'])
def giris():
    form = GirisFormu()
    if form.validate_on_submit():
        email = form.email.data
        sifre = form.sifre.data
        # Giriş işlemlerini burada gerçekleştirin (örneğin, kullanıcı doğrulama)
        return f"Giriş başarılı! Email: {email}"
    return render_template('giris.html', form=form)


# SQLAlchemy - Veritabanı işlemleri için kullanılır. SQLAlchemy, Python programlama dilinde kullanılan bir veritabanı araç takımıdır. SQLAlchemy, veritabanı işlemlerini daha kolay ve esnek hale getirmek için bir Object-Relational Mapping (ORM) sistemi sağlar. ORM, veritabanındaki tabloları Python sınıflarına dönüştürerek, veritabanı işlemlerini nesne yönelimli bir şekilde gerçekleştirmenizi sağlar. SQLAlchemy, farklı veritabanı türlerini destekler ve veritabanı sorgularını Python kodu ile yazmanıza olanak tanır. Bu sayede, veritabanı işlemlerini daha hızlı ve güvenli bir şekilde gerçekleştirebilirsiniz.

if __name__ == "__main__":
    app.run(debug=True)
