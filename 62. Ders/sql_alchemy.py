from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)

# Kullanılacak db cinsi belirtilir
# /// 3 slash dosya proje klasöründe oluşturulacak demektir
# PostgreSQL için 'postgresql://username:password@localhost/database_name' şeklinde yazılır
# MySQL için 'mysql://username:password@localhost/database_name' şeklinde yazılır

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # SQLAlchemy nesnesi oluşturuluyor


# Model oluşturulması
# dM = [@gmail.com] = doğrulanmış mailler

class Kullanici(db.Model):
    # id alanı, birincil anahtar olarak tanımlanır
    id = db.Column(db.Integer, primary_key=True)
    kullanici_adi = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(125), nullable=False)
    sifre = db.Column(db.String(75), nullable=False)

    gonderiler = db.relationship('Gonderi', backref='yazar', lazy=True)

    def __repr__(self):
        return f"Kullanici('{self.kullanici_adi}', '{self.email}')"


class Gonderi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    baslik = db.Column(db.String(100), nullable=False)
    icerik = db.Column(db.Text, nullable=False)

    tarih = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )

    kullanici_id = db.Column(
        db.Integer,
        db.ForeignKey('kullanici.id'),
        nullable=False
    )

    def __repr__(self):
        return f"Gonderi('{self.baslik}', '{self.tarih}')"


if __name__ == "__main__":
    app.run(debug=True)
