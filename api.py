from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kelurahan.db'
api = Api(app)
db = SQLAlchemy(app)


class Kelurahan(db.Model):
    id_kelurahan = db.Column(db.Integer, primary_key=True)
    kode_kelurahan = db.Column(db.String(10))
    nama_kelurahan = db.Column(db.String(100))


class KelurahanAPI(Resource):
    def get(self):
        kelurahan = Kelurahan.query.all()
        result = []
        for k in kelurahan:
            result.append({
                'id_kelurahan': k.id_kelurahan,
                'kode_kelurahan': k.kode_kelurahan,
                'nama_kelurahan': k.nama_kelurahan
            })
        return result

    def post(self):
        data = request.get_json()
        kelurahan = Kelurahan(
            kode_kelurahan=data['kode_kelurahan'], nama_kelurahan=data['nama_kelurahan'])
        db.session.add(kelurahan)
        db.session.commit()
        return {'message': 'Kelurahan berhasil ditambahkan'}

    def put(self):
        data = request.get_json()
        kelurahan = Kelurahan.query.filter_by(
            id_kelurahan=data['id_kelurahan']).first()
        if kelurahan is None:
            return {'message': 'Kelurahan tidak ditemukan'}
        kelurahan.kode_kelurahan = data['kode_kelurahan']
        kelurahan.nama_kelurahan = data['nama_kelurahan']
        db.session.commit()
        return {'message': 'Kelurahan berhasil diubah'}

    def delete(self):
        data = request.get_json()
        kelurahan = Kelurahan.query.filter_by(
            id_kelurahan=data['id_kelurahan']).first()
        if kelurahan is None:
            return {'message': 'Kelurahan tidak ditemukan'}
        db.session.delete(kelurahan)
        db.session.commit()
        return {'message': 'Kelurahan berhasil dihapus'}


api.add_resource(KelurahanAPI, '/kelurahan')

if __name__ == '__main__':
    app.run(debug=True)
