
import hdfs
from flask import request


def do_hdfs_upload(url, myid, keyhash, fname, fdata, ftag):
    # talk to MDS about file owner
    resp = endorse(fname, "owner", keyhash)
    if resp.status_code != 200
        return resp

    # create hdfs client on demand now. No need to optimize for PoC
    hdfs_client = hdfs.InsecureClient(url, user=ftag)
    hdfs_client.write(fname, fdata, overwrite=True, permission=0666, encoding="utf-8")
    return "OK"

