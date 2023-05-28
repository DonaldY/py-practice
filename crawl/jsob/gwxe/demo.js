var jen = require( "./jen" );

function execute(str) {
    let jsEncrypt = new jen.JSEncrypt();
    let key = '-----BEGIN PUBLIC KEY-----MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAr0c+W5cCGb0D3Fmeu4Z0wZfGt3Or1zRNLL226mxZPRwXz56mEeBdxg3nwQvh/Qcw4lF1vA6mqkhoY4RCmoKSafs9rXaNrnUhqFFjaUQwtzEO1rK/Lrb9pvYEBdFAPmiXfF2KAsMM7t4qpAjB5FPC//oxX22pNPuz7lltGcIbzHa5N3pgIy9p1bnG2qPV+lGzWrMVtOhBxOqrN66Iix0tpVDaS+wKdy2XvDoapPg/pr+Nsip80XLdCbtFCHGyGiEoVaLgqGH6ZScuOjVPmzbfB2kvc5IcM/53tvEWvdCyEn7ct5dAXZbXBrX0rjl4lJz/U5ZgHenTXRV4nrEmsgxQYwIDAQAB-----END PUBLIC KEY-----';
    jsEncrypt.setKey(key);
    return jsEncrypt.encrypt(str);
}

function base64En(str) {
    let result = encodeURIComponent(str);
    result = unescape(result);
    return btoa(result);
}

let str1 = '_953501_ajBcuCYsbkFg3xv2ecFLo34_d0c0i7c1hjt576l9rijk55kujdEDwuIeRXt01QQFeQsqMUYr';

let encryptStr = execute(str1);

console.log(base64En(encryptStr));