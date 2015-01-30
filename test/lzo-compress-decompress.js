var lzo = require('../');
var assert = require('assert');

var data, input, output, compressedLen, compressed, decompressedLen, decompressed;

data = "hello world; hello world; hello world;";

input = new Buffer(data);
output = new Buffer(100);

compressedLen = lzo.compress(input, output);
compressed = output.slice(0, compressedLen);
input = Buffer.concat([compressed, new Buffer('hello')]);
output = new Buffer(100);

result = lzo.decompress(input, output);
decompressedLen = result[1];
decompressed = output.slice(0, decompressedLen);

assert.equal(data, decompressed.toString());
