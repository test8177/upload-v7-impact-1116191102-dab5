import hashlib,json,re,subprocess,sys
raw=subprocess.run(['id'],check=True,capture_output=True).stdout
effect=bool(re.match(rb'^uid=[0-9]+\([^\r\n]+\) gid=[0-9]+\([^\r\n]+\)',raw))
print('PAGES_CRITICAL_RESULT '+json.dumps({'benign_id_effect':effect,'effect_bytes':len(raw),'effect_sha256':hashlib.sha256(raw).hexdigest()},sort_keys=True,separators=(',',':')))
sys.exit(0 if effect else 1)
