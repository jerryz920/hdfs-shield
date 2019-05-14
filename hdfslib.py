
import hdfs
from flask import request


def do_hdfs_upload(myid, url, safe_url, keyhash, fname, fdata, ftag):
    # talk to MDS about file owner
    resp = endorse(fname, "owner", keyhash)
    if resp.status_code != 200:
        return resp

    # create hdfs client on demand now. No need to optimize for PoC
    hdfs_client = hdfs.InsecureClient(url, user=ftag)
    return hdfs_client.write(fname, fdata, overwrite=True, permission=666)

