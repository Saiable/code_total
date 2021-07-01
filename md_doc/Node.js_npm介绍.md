[TOC]

# npm介绍

## 模块[¶](#_1)

## 包[¶](#_2)

包描述文件: package.json

## NPM(Node Package Mannager)[¶](#npmnode-package-mannager)

- CommonJS包规范是理论，NPM是其中的一个实践。
- 对于Node而言，NPM帮助其完成了第三方模块的发布、安装和依赖等。借助NPM，Node与第三方模块之间形成了很好的一个生态系统。

### NPM命令[¶](#npm)

- npm -v：查看npm的版本

```
F:\workspace\npm\hellonpm>npm -v
6.14.4
```

- npm version：查看所有模块的版本

```
F:\workspace\npm\hellonpm>npm version
{
  hellonpm: '1.0.0',
  npm: '6.14.4',
  ares: '1.15.0',
  brotli: '1.0.7',
  cldr: '36.0',
  http_parser: '2.9.3',
  icu: '65.1',
  llhttp: '2.0.4',
  modules: '72',
  napi: '5',
  nghttp2: '1.40.0',
  node: '12.16.2',
  openssl: '1.1.1e',
  tz: '2019c',
  unicode: '12.1',
  uv: '1.34.2',
  v8: '7.8.279.23-node.34',
  zlib: '1.2.11'
}
```

- npm：帮助说明

```
F:\workspace\npm\hellonpm>npm

Usage: npm <command>

where <command> is one of:
    access, adduser, audit, bin, bugs, c, cache, ci, cit,
    clean-install, clean-install-test, completion, config,
    create, ddp, dedupe, deprecate, dist-tag, docs, doctor,
    edit, explore, fund, get, help, help-search, hook, i, init,
    install, install-ci-test, install-test, it, link, list, ln,
    login, logout, ls, org, outdated, owner, pack, ping, prefix,
    profile, prune, publish, rb, rebuild, repo, restart, root,
    run, run-script, s, se, search, set, shrinkwrap, star,
    stars, start, stop, t, team, test, token, tst, un,
    uninstall, unpublish, unstar, up, update, v, version, view,
    whoami

npm <command> -h  quick help on <command>
npm -l            display full usage info
npm help <term>   search for help on <term>
npm help npm      involved overview

Specify configs in the ini-formatted file:
    C:\Users\Administrator\.npmrc
or on the command line via: npm <command> --key value
Config info can be viewed via: npm help config

npm@6.14.4 F:\Program Files\nodejs\node_modules\npm
```

- npm search 包名：模块包

```
F:\workspace\npm\hellonpm>npm search math
NAME                      | DESCRIPTION          | AUTHOR          | DATE

math                      | Mathematical…        | =kzh            | 2011-09-19

Math                      | This package name…   | =npm            | 2016-06-14

math-expression-evaluator | A flexible math…     | =bugwheels94    | 2020-12-20

mathjs                    | Math.js is an…       | =josdejong      | 2021-02-03

simple-statistics         | Simple Statistics    | =tmcw           | 2021-03-02

node-int64                | Support for…         | =broofa…        | 2015-04-0
4
long                      | A Long class for…    | =dcode          | 2018-02-03

katex                     | Fast math…           | =edemaine…      | 2020-07-1
2
is-number                 | Returns true if a…   | =doowb…         | 2018-07-0
4
dompurify                 | DOMPurify is a…      | =cure53         | 2020-12-18

jsbn                      | The jsbn library is… | =andyperlitch   | 2017-02-13

big-integer               | An arbitrary length… | =peterolson     | 2019-11-11

nerdamer                  | javascript…          | =brosnanyuen…   | 2021-02-1
5
hull.js                   | JavaScript library…  | =andriiheonia   | 2020-10-24

clamp                     | Clamp a value…       | =hughsk         | 2014-07-29

num2fraction              | Convert number to…   | =yisi           | 2015-09-14

math-interval-parser      | Parse math interval  | =semigradsky    | 2019-01-09

math.log1p                | An…                  | =ljharb         | 2020-12-25

fraction.js               | A rational number…   | =infusion       | 2020-12-22

mathml                    | MathML allows to…    | =physikerwelt   | 2020-11-12
```

- npm init：创建package.json

```
F:\workspace\npm\hellonpm>npm init
This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help json` for definitive documentation on these fields
and exactly what they do.

Use `npm install <pkg>` afterwards to install a package and
save it as a dependency in the package.json file.

Press ^C at any time to quit.
package name: (hellonpm)
version: (1.0.0)
description: npm init test
entry point: (index.js)
test command:
git repository:
keywords:
author: test
license: (ISC)
About to write to F:\workspace\npm\hellonpm\package.json:

{
  "name": "hellonpm",
  "version": "1.0.0",
  "description": "npm init test",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "test",
  "license": "ISC"
}


Is this OK? (yes) yes
```

- npm install/i 包名:在当前目录安装包

```
F:\workspace\npm\hellonpm>npm install math
npm notice created a lockfile as package-lock.json. You should commit this file.

npm WARN hellonpm@1.0.0 No repository field.

+ math@0.0.3
added 1 package from 1 contributor and audited 1 package in 1.307s
found 0 vulnerabilities
```

- node index.js:创建js文件，调用math模块，执行index.js

```
//index.js
var math = require("math");
console.log(math);
```

调用index.js

```
F:\workspace\npm\hellonpm>node index.js
Object [Math] {
  samesign: [Function],
  copysign: [Function],
  add: [Function],
  sum: [Function],
  mul: [Function],
  prod: [Function],
  factorial: [Function],
  gcd: [Function],
  lcm: [Function]
}
```

- npm remove/i 包名：删除包

```
F:\workspace\npm\hellonpm>npm remove math
npm WARN hellonpm@1.0.0 No repository field.

removed 1 package in 1.344s
found 0 vulnerabilities
```

- npm install 包名 --save：安装包并添加到依赖中

```
F:\workspace\npm\hellonpm>npm i math --save
npm WARN hellonpm@1.0.0 No repository field.

+ math@0.0.3
added 1 package from 1 contributor and audited 1 package in 1.621s
found 0 vulnerabilities
//package.json中新增了dependencies字段
  "dependencies": {
    "math": "0.0.3"
  }
```

当package.json有`dependecies`字段时，可以直接执行`npm install`，会自动将该字段里面的包安装上，而不需要指定包名；

- npm install 包名 -g：全局模式安装包（全局安装的包，一般都是一些工具）

### 配置CNPM[¶](#cnpm)

```
npm install -g cnpm --registry=https://registry.npm.taobao.org
```

通过cnpm安装的包，文件命名和官方npm有些许不同，但不影响工具的使用

```
//npm安装express模块，耗时18.317s
+ express@4.17.1
added 50 packages from 37 contributors and audited 51 packages in 18.317s

//cnpm安装express模块，耗时5s
√ All packages installed (52 packages installed from npm registry, used 5s(network 5s), speed 143.42kB/s, json 49(122.94kB), tarball 547.69kB)
```

### node搜索包的流程[¶](#node)

通过npm下载的包都放在node_modules文件夹中，我们通过npm下载的包，直接通过包名引入即可

node在使用模块名字来引入模块时，它会首先在当前目录的node_modules中寻找是否含有该模块

- 如果有则直接使用，如果没有则去上一级目录的mode_modules中寻找
- 如果有则直接使用，如果没有则去上一级目录寻找，知道找到为止
- 直到找到磁盘的根目录，如果依然没有，则报错