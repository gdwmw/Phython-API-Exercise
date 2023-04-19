import os.path
from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

# config database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model Provinsi
class Provinsi(db.Model):
    id_provinsi = db.Column(db.Integer, primary_key=True)
    kode_provinsi = db.Column(db.String(10))
    nama_provinsi = db.Column(db.String(100))

# Model Kabupaten Kota
class KabKota(db.Model):
    id_kab_kota = db.Column(db.Integer, primary_key=True)
    kode_kab_kota = db.Column(db.String(10))
    nama_kab_kota = db.Column(db.String(100))

# Model Kelurahan/desa
class Kelurahan(db.Model):
    id_kelurahan = db.Column(db.Integer, primary_key=True)
    kode_kelurahan = db.Column(db.String(10))
    nama_kelurahan = db.Column(db.String(100))

# Model Kecamatan
class Kecamatan(db.Model):
    id_kecamatan = db.Column(db.Integer, primary_key=True)
    kode_kecamatan = db.Column(db.String(10))
    nama_kecamatan = db.Column(db.String(100))


# Resource provinsi
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
        return result, 200

    def post(self):
        data = request.get_json()
        provinsi = Provinsi(kode_provinsi=data['kode_provinsi'], nama_provinsi=data['nama_provinsi'])
        db.session.add(provinsi)
        db.session.commit()
        return {'message': 'Provinsi berhasil ditambahkan'}, 201

    def put(self):
        data = request.get_json()
        provinsi = Provinsi.query.filter_by(id_provinsi=data['id_provinsi']).first()
        if provinsi is None:
            return {'message': 'Provinsi tidak ditemukan'}, 404
        provinsi.kode_provinsi = data['kode_provinsi']
        provinsi.nama_provinsi = data['nama_provinsi']
        db.session.commit()
        return {'message': 'Provinsi berhasil diubah'}, 200

    def delete(self):
        data = request.get_json()
        provinsi = Provinsi.query.filter_by(
            id_provinsi=data['id_provinsi']).first()
        if provinsi is None:
            return {'message': 'Provinsi tidak ditemukan'}, 404
        db.session.delete(provinsi)
        db.session.commit()
        return {'message': 'Provinsi berhasil dihapus'}, 200


# Resource kab kota
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
        return result, 200

    def post(self):
        data = request.get_json()
        kabkota = KabKota(kode_kab_kota=data['kode_kab_kota'], nama_kab_kota=data['nama_kab_kota'])
        db.session.add(kabkota)
        db.session.commit()
        return {'message': 'Kab/Kota berhasil ditambahkan'}, 201

    def put(self):
        data = request.get_json()
        kabkota = KabKota.query.filter_by(id_kab_kota=data['id_kab_kota']).first()
        if kabkota is None:
            return {'message': 'Kab/Kota tidak ditemukan'}, 404
        kabkota.kode_kab_kota = data['kode_kab_kota']
        kabkota.nama_kab_kota = data['nama_kab_kota']
        db.session.commit()
        return {'message': 'Kab/Kota berhasil diubah'}, 200

    def delete(self):
        data = request.get_json()
        kabkota = KabKota.query.filter_by(id_kab_kota=data['id_kab_kota']).first()
        if kabkota is None:
            return {'message': 'Kab/Kota tidak ditemukan'}, 404
        db.session.delete(kabkota)
        db.session.commit()
        return {'message': 'Kab/Kota berhasil dihapus'}, 200


# Resource kecamatana
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
        return result, 200

    def post(self):
        data = request.get_json()
        kecamatan = Kecamatan( kode_kecamatan=data['kode_kecamatan'], nama_kecamatan=data['nama_kecamatan'])
        db.session.add(kecamatan)
        db.session.commit()
        return {'message': 'Kecamatan berhasil ditambahkan'}, 201

    def put(self):
        data = request.get_json()
        kecamatan = Kecamatan.query.filter_by( id_kecamatan=data['id_kecamatan']).first()
        if kecamatan is None:
            return {'message': 'Kecamatan tidak ditemukan'}, 404
        kecamatan.kode_kecamatan = data['kode_kecamatan']
        kecamatan.nama_kecamatan = data['nama_kecamatan']
        db.session.commit()
        return {'message': 'Kecamatan berhasil diubah'}, 200

    def delete(self):
        data = request.get_json()
        kecamatan = Kecamatan.query.filter_by(id_kecamatan=data['id_kecamatan']).first()
        if kecamatan is None:
            return {'message': 'Kecamatan tidak ditemukan'}, 404
        db.session.delete(kecamatan)
        db.session.commit()
        return {'message': 'Kecamatan berhasil dihapus'}, 200


# Resource kelurahan / desa
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
        return result, 200

    def post(self):
        data = request.get_json()
        kelurahan = Kelurahan(kode_kelurahan=data['kode_kelurahan'], nama_kelurahan=data['nama_kelurahan'])
        db.session.add(kelurahan)
        db.session.commit()
        return {'message': 'Kelurahan berhasil ditambahkan'}, 201

    def put(self):
        data = request.get_json()
        kelurahan = Kelurahan.query.filter_by(id_kelurahan=data['id_kelurahan']).first()
        if kelurahan is None:
            return {'message': 'Kelurahan tidak ditemukan'}, 404
        kelurahan.kode_kelurahan = data['kode_kelurahan']
        kelurahan.nama_kelurahan = data['nama_kelurahan']
        db.session.commit()

        return {'message': 'Kelurahan berhasil diubah'}, 200

    def delete(self):
        data = request.get_json()
        kelurahan = Kelurahan.query.filter_by(id_kelurahan=data['id_kelurahan']).first()
        if kelurahan is None:
            return {'message': 'Kelurahan tidak ditemukan'}, 404
        db.session.delete(kelurahan)
        db.session.commit()
        return {'message': 'Kelurahan berhasil dihapus'}, 200


with app.app_context():
    db.create_all()

api.add_resource(ProvinsiAPI, '/provinsi')
api.add_resource(KabKotaAPI, '/kabkota')
api.add_resource(KecamatanAPI, '/kecamatan')
api.add_resource(KelurahanAPI, '/kelurahan')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
