# Young Tista

This is a simple Python CLI tool to interact with GPT-3's completion API. Fed the AI my past blog posts and used it to be able to ask anything to my younger me.

## Running In The CLI

```shell
$ git clone git@github.com:tistaharahap/young-tista.git
$ cd young-tista
$ poetry shell
$ poetry install
$ tista --help
```

When you run without the `--help` flag, it will ask you to input a question. The question will be sent to the AI and the response will be printed out.

## Running As An API

```shell
$ git clone git@github.com:tistaharahap/young-tista.git
$ cd young-tista
$ poetry shell
$ poetry install
$ cp run-api.sh.example run-api.sh
$ vim run-api.sh # edit the env vars
$ ./run-api.sh
```

You need MongoDB to store the questions.

## Credit

Read a tweet by [Michelle Huang](https://twitter.com/michellehuang42) and worked on based on her work.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">i&#39;ve received a lot of requests on how to replicate my AI experiment so here goes --<br><br>[tutorial] how to create your own &quot;inner child&quot; chatbot using GPT-3<a href="https://t.co/lsWcUK7RYA">https://t.co/lsWcUK7RYA</a></p>&mdash; michelle huang (@michellehuang42) <a href="https://twitter.com/michellehuang42/status/1597702974889144320?ref_src=twsrc%5Etfw">November 29, 2022</a></blockquote>
