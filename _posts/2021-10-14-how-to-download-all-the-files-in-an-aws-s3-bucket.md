---
layout: post
title: "How to download all the files in an AWS S3 Bucket?"
date: 2021-10-14
description: "Unfortunately AWS S3 Console doesn’t have an option to download all the content of an S3 bucket at the moment, but there are other options…"
image: https://cdn-images-1.medium.com/max/800/0*iRM5kMJ8BsjNVm05.jpg
---

### How to download all the files in an AWS S3 Bucket?

![](https://cdn-images-1.medium.com/max/800/0*iRM5kMJ8BsjNVm05.jpg)*Image from YouTube: <https://www.youtube.com/watch?v=4phTbiG5Dgg>*

Unfortunately AWS S3 Console doesn’t have an option to download all the content of an S3 bucket at the moment, but there are other options like AWS CLI to do so.

First you need to install the CLI with one of the following commands:

```
sudo pip install awscli
```

or

```
sudo easy_install awscli
```

Once installed, you can then use the following command:

```
aws s3 sync s3://<your_source_s3_bucket> <your_local_path>
```

For instance:

```
aws s3 sync s3://all_my_stuff_bucket .
```

This command will start downloading all the objects in `all_my_stuff_bucket` to the current directory.

The output will looks something like this:

```
download: s3://all_my_stuff_bucket/file1.txt to file1.txtdownload: s3://all_my_stuff_bucket/file2.txt to file2.txtdownload: s3://all_my_stuff_bucket/file3.txt to file3.txt
```

Notes:

1. This will not touch or change anything in your S3 bucket.
2. This will not delete anything in your destination folder.
3. If you want to delete any existing files in your current folder you can include `--delete` argument.

Interesting thing about this sync command is, you can use it to copy from one S3 bucket to another or from your local to an S3 bucket.

For more examples you can check the official documentation of this command here:

[**sync - AWS CLI 1.20.61 Command Reference**  
*(boolean) Displays the operations that would be performed using the specified command without actually running them…*docs.aws.amazon.com](https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html "https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html")

If your bucket has many nested folders, you can download the whole folder recursively with the following command:

`aws s3 cp s3://all_my_stuff_bucket/paths/child_fodlers local_folder --recursive`

I found this “sync” CLI very useful for many use-cases, so I hope you find it useful too!

Cheers!
