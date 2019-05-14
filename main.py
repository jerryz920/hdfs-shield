#!/usr/bin/env python3

from flask import request as frequest
from server import create, run
import sys
import utils
from hdfslib import do_hdfs_upload
from api import define_tag

app=create(__name__)
myid=None
hdfs_url="http://hdfs-1.latte.org:9000"
safe_url="http://mds"


@app.route('/upload', methods=['PUT'])
def upload_hdfs():
    return do_hdfs_upload(
            myid,
            hdfs_url,
            safe_url
            utils.keyhash(frequest.environ["peercert"]),
            frequest.form["filename"],
            frequest.files["file"],
            frequest.form["tagname"])

@app.route('/define_tag', methods=['PUT', 'POST'])
def define_tag():
    return define_tag(
            myid,
            safe_url,
            utils.keyhash(frequest.environ["peercert"]),
            frequest.form["tagname"],
            frequest.form["policy"])


if __name__ == "__main__":
    ca_cert = "/var/run/secrets/kubernetes.io/serviceaccount/ca.crt"
    cert = "/opt/creds/server.crt"
    key = "/opt/creds/server.key"
    if len(sys.argv) >= 4:
        ca_cert = sys.argv[1]
        cert = sys.argv[2]
        key = sys.argv[3]

    run(app, "0.0.0.0", 20000, ca_cert, cert, key)


