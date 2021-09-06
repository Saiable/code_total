const path = require('path');

function resolve(dir) {
  return path.join(__dirname, dir);
}
console.log(__dirname)
console.log(path.join(__dirname,'src/assets'))
module.exports = {
  // publicPath: './ ',
  // baseUrl : './',
  lintOnSave: true,
  chainWebpack: (config) => {
    config.resolve.alias
      .set('@',resolve('src'))
      .set('assets',resolve('src/assets'))
      .set('common',resolve('src/common'))
      .set('components',resolve('src/components'))
      .set('network',resolve('src/network'))
      .set('views',resolve('src/views'))
  }
};
