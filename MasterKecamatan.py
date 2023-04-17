from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kecamatan.db'
api = Api(app)
db = SQLAlchemy(app)


class Kecamatan(db.Model):
    id_kecamatan = db.Column(db.Integer, primary_key=True)
    kode_kecamatan = db.Column(db.String(10))
    nama_kecamatan = db.Column(db.String(100))


class KecamatanAPI(Resource):
    def get(self):
        kecamatan = Kecamatan.query.all()
        result = []
        for k in kecamatan:
            result.append({
                'id_kecamatan': k.id_kecamatan,
                'kode_kecamatan': k.kode_kecamatan,
                'nama_kecamatan': k.nama_kecamatan
            })
        return result

    def post(self):
        data = request.get_json()
        kecamatan = Kecamatan(
            kode_kecamatan=data['kode_kecamatan'], nama_kecamatan=data['nama_kecamatan'])
        db.session.add(kecamatan)
        db.session.commit()
        return {'message': 'Kecamatan berhasil ditambahkan'}

    def put(self):
        data = request.get_json()
        kecamatan = Kecamatan.query.filter_by(
            id_kecamatan=data['id_kecamatan']).first()
        if kecamatan is None:
            return {'message': 'Kecamatan tidak ditemukan'}
        kecamatan.kode_kecamatan = data['kode_kecamatan']
        kecamatan.nama_kecamatan = data['nama_kecamatan']
        db.session.commit()
        return {'message': 'Kecamatan berhasil diubah'}

    def delete(self):
        data = request.get_json()
        kecamatan = Kecamatan.query.filter_by(
            id_kecamatan=data['id_kecamatan']).first()
        if kecamatan is None:
            return {'message': 'Kecamatan tidak ditemukan'}
        db.session.delete(kecamatan)
        db.session.commit()
        return {'message': 'Kecamatan berhasil dihapus'}


api.add_resource(KecamatanAPI, '/kecamatan')

if __name__ == '__main__':
    app.run(debug=True)
