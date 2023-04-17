from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///provinsi.db'
api = Api(app)
db = SQLAlchemy(app)


class Provinsi(db.Model):
    id_provinsi = db.Column(db.Integer, primary_key=True)
    kode_provinsi = db.Column(db.String(10))
    nama_provinsi = db.Column(db.String(100))


class ProvinsiAPI(Resource):
    def get(self):
        provinsi = Provinsi.query.all()
        result = []
        for p in provinsi:
            result.append({
                'id_provinsi': p.id_provinsi,
                'kode_provinsi': p.kode_provinsi,
                'nama_provinsi': p.nama_provinsi
            })
        return result

    def post(self):
        data = request.get_json()
        provinsi = Provinsi(
            kode_provinsi=data['kode_provinsi'], nama_provinsi=data['nama_provinsi'])
        db.session.add(provinsi)
        db.session.commit()
        return {'message': 'Provinsi berhasil ditambahkan'}

    def put(self):
        data = request.get_json()
        provinsi = Provinsi.query.filter_by(
            id_provinsi=data['id_provinsi']).first()
        if provinsi is None:
            return {'message': 'Provinsi tidak ditemukan'}
        provinsi.kode_provinsi = data['kode_provinsi']
        provinsi.nama_provinsi = data['nama_provinsi']
        db.session.commit()
        return {'message': 'Provinsi berhasil diubah'}

    def delete(self):
        data = request.get_json()
        provinsi = Provinsi.query.filter_by(
            id_provinsi=data['id_provinsi']).first()
        if provinsi is None:
            return {'message': 'Provinsi tidak ditemukan'}
        db.session.delete(provinsi)
        db.session.commit()
        return {'message': 'Provinsi berhasil dihapus'}


api.add_resource(ProvinsiAPI, '/provinsi')

if __name__ == '__main__':
    app.run(debug=True)
