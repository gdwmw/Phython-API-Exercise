from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kabkota.db'
api = Api(app)
db = SQLAlchemy(app)


class KabKota(db.Model):
    id_kab_kota = db.Column(db.Integer, primary_key=True)
    kode_kab_kota = db.Column(db.String(10))
    nama_kab_kota = db.Column(db.String(100))


class KabKotaAPI(Resource):
    def get(self):
        kabkota = KabKota.query.all()
        result = []
        for kk in kabkota:
            result.append({
                'id_kab_kota': kk.id_kab_kota,
                'kode_kab_kota': kk.kode_kab_kota,
                'nama_kab_kota': kk.nama_kab_kota
            })
        return result

    def post(self):
        data = request.get_json()
        kabkota = KabKota(
            kode_kab_kota=data['kode_kab_kota'], nama_kab_kota=data['nama_kab_kota'])
        db.session.add(kabkota)
        db.session.commit()
        return {'message': 'Kab/Kota berhasil ditambahkan'}

    def put(self):
        data = request.get_json()
        kabkota = KabKota.query.filter_by(
            id_kab_kota=data['id_kab_kota']).first()
        if kabkota is None:
            return {'message': 'Kab/Kota tidak ditemukan'}
        kabkota.kode_kab_kota = data['kode_kab_kota']
        kabkota.nama_kab_kota = data['nama_kab_kota']
        db.session.commit()
        return {'message': 'Kab/Kota berhasil diubah'}

    def delete(self):
        data = request.get_json()
        kabkota = KabKota.query.filter_by(
            id_kab_kota=data['id_kab_kota']).first()
        if kabkota is None:
            return {'message': 'Kab/Kota tidak ditemukan'}
        db.session.delete(kabkota)
        db.session.commit()
        return {'message': 'Kab/Kota berhasil dihapus'}


api.add_resource(KabKotaAPI, '/kabkota')

if __name__ == '__main__':
    app.run(debug=True)
