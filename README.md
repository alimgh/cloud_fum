

## به نام خدا
                                      

## اعضای گروه:

 1. علی مقدس زاده
 2. کنعان باقری
 3. زهرا لطفی



# مقدمه

یک سیستم کتابفروشی پیاده سازی کرده ایم که تعدادی کاربر، کتاب و یک سری تراکنش ها در این سیستم درنظر گرفته شده است و قسمتی هم برای نظرات، انتقادات و پیشنهادات وجود دارد

منظور از تراکنش در این پروژه به این صورت است که شخص فروشنده و خریدار را مشخص میکند. در ادامه به توضیح هر کدام از بخش های پروژه میپردازیم

 **نکته**  : کدهای پروژه توسط خود اعضای گروه پیاده سازی شده است

# کاربر

هنگامی که کاربر ثبت نام میکند از او اطلاعاتی مانند
 username  ,password وtype
. فروشنده یا خریدار) دریافت میشود)

در آینده هم اگر نیاز به تغییرات و پیچیده تر شدن سیستم بود میتوان با اضافه کردن نمره یا تبدیل
 کاربر ها به دو تایپ مختلف این کار را انجام داد

این سیستم باید ویژگی هایی مانند اضافه کردن، حذف و ویرایش کاربر را داشته باشد که البته هدف اصلی این است که یک سرویس ساده به میکروسرویس تبدیل شود


# کتاب

بخش اصلی و مهم سرویس، بخش کتاب است. در این قسمت لیستی از کتاب ها که دارای مشخصاتی مانند( عنوان، قیمت، نویسنده، انتشارات، خلاصه، ژانر و...)ذخیره میشوند

از ویژگی های این بخش میتوان به اضافه و حذف کردن کتاب، ویرایش اطلاعات و جستجوی پیشرفته اشاره کرد

در قسمت نظرات میتوانیم نظر های مختلفی از یک کاربر داشته باشیم و هرکتاب و کاربر میتواند چندین نظر مختلف دریافت و ایجاد کند و میتوانیم با هوش مصنوعی تشخیص بدهیم این نظر مثبت است یا منفی

## فروش

در این قسمت یک جدول اصلی به نام جدول سفارشات وجود دارد که تعیین میکند چه کتابی توسط چه کاربری به چه شخصی فروخته شده است. نوعی تعامل بین سرویس های کاربر و کتاب وجود دارد که بخش حساس سرویس محسوب میشود

بخشی به نام وضعیت سفارش هم وجود دارد که مراحل سفارش مانند در حال آماده سازی است، تایید شده یا تحویل داده شده است را تعیین میکند. در پایان تحویل سفارش نیز از کاربر درخواست میشود که نظر خود را ثبت کند

حتی میتوان بخشی را در نظر گرفت که خریدار به فروشنده امتیاز دهد که در این صورت میتوانیم میانگین امتیاز هم داشته باشیم

## هوش مصنوعی

یک سرویس خیلی ساده است که متنی را دریافت میکند و یک برچسب مثبت یا منفی به آن میدهد که مشخص میکند نظر مثبت یا منفی است

## در پایان

از دلایلی که  چرا هر بخش را میکرو سرویس میکنیم میتوان گفت در بخش کاربر بخشی است که همه قسمت ها با آن تعامل دارند و یک بخشی است که اطلاعات کاربران در آن قرار میگیرد، به همین دلیل محرمانگی خاصی میتواند داشته باشد و این قسمت ارزش میکرو سرویس کردن جدا را دارد تا درآینده کنترل بهتری به آن داشته باشیم

در بحث کتابخانه و سفارشات، در حوزه کتابگردی خب سرویسی است که از همه امنیت کمتری دارد اما در بعضی از شرایط ممکن است برخی از کاربران فقط بخواهند اطلاعاتی از یک کتاب را مشاهده یا  اضافه کنند به همین خاطر ممکن است در یک بازه زمانی شلوغی و فشار خاصی در این بخش به وجود بیاید

سفارشات عموما وابستگی زیادی به کتاب ها دارد اما خود این بخش سیستم مستقلی است. ممکن است که شخص پیگیری سفارش خود را داشته باشد و لزوما با قسمت کتاب ها کاری نداشته باشد. حتی دراینده میتوان درگاه بانکی به آن اضافه کرد و بخاطر مباحث امنیتی و ... باعث میشود رویکرد متفاوتی به آن داشت

یا دریک بازه های زمانی خاصی ممکن است سرویس کتاب ها وسفارشات سنگین شود این به تنهایی توجیه و دلیل خوبی برای میکرو سرویس جدا دارد

در دیتا بیس هم مشخص است که هرکدام جدول خاصی دارند که با آن در ارتباط اند و ارتباطاتی در آن وجود دارد که کمتر به صورت جدی استفاده میشود که اطلاعاتی را دریافت کند

برای قسمت هوش مصنوعی هم این سرویس اولویت خیلی پایینی دارد و سرویسی است که اصلا نیاز به دیتابیس ندارد اما نکته ای که وجود دارد این است که از منابع متفاوتی استفاده میکند و همین ها دلایلی میتواند باشد که میکروسرویس جدا شود و حتی گاهی اوقات بخاطر اهمیت کمتر غیرفعال شود

پس در کل 4 میکرو سرویس وجود دارد که پیاده سازی کرده ایم


## دیاگرام ها

[برای نمایش دیاگرام ها روی من کلیک کنید](https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Cloud#R%3Cmxfile%20pages=%223%22%3E%3Cdiagram%20id=%22Yx9fCsJXSSdDCp3vd9yJ%22%20name=%22Access%22%3E3Vtbc9o6EP41PLZjyTfymJCk7Zx0mpnMmZ48ClvBamyLkQWB/Poj2RJYNhACgqh5IdZ6Jdt7%2bbTf2hn4o2LxjaFp9pOmOB9AL10M/OsBhMDzh%2bKPlCwbSQhBI5gwkiqlteCBvGI9U0lnJMWVocgpzTmZmsKEliVOuCFDjNEXU%2b2J5uZVp2iCe4KHBOV96W%2bS8qyRDkNvLf%2bOySTTVwaeOlMgrawEVYZS%2btIS%2bTcDf8Qo5c1RsRjhXBpP26WZd7vl7OrGGC75PhNe/3nx7pfR6HcURPfZ4%2bjp1w3/AtQyFV/qJ8apMIAaUsYzOqElym/W0itGZ2WK5bKeGK117iidCiEQwj%2bY86XyJppxKkQZL3J1Fi8I/09O/xqq0aMxul6otevBsjW4x4wUmGOmZSVny2apONTjx/bJ9Vr1SC/Wt562BJ2xBO8ymYpCxCaY79CLGz1pztYFlG%2b%2bYSoegy2FAsM54mRuxhtSYTtZ6a09Kw6Uc9/haBg0C89RPlOXeiCTUk6TP6hMxa%2bSzKYbg%2bIOjUVyG45EuZzhXyfCitInV3PMOBHZc6lOFCRNm5jBFXlF43o9af8pJSWvHzK8GoTXGz2yM2LllfBisAED1FWMNDMsrmZ98b56ngebuQqe/Ga0t0/U4vfyaVoq9OmpEsHRddrqHg73I4g%2bTcI6lq%2bR7Xytp14yhpYtBRX3/dBRQRn6nhGQej%2b53Vc/2q0fwHCXvjho7thq0MKoDz4YsSRzGWf0PR%2bNMwJmwNA3rK6D0mGciT8NzrhWGAydAJrIN0PyLaDp6vvgDMChr9kCjl8sFU6G3pjSZ124RLmw99VYiKMJryOv0eEMJc%2bknLgMM7FFmPFhB2ag8zDT8%2b9oVnGxLOv5TPCnqTycFfllwmnbPbUr72lFOKHSTWPKxRob/MclDrU9vjXbe/7YavcoMnfgWA1f1nRR79FZiynqWdYrfeA7hNxH4LYB2uti0Tpswz1h2zE%2b10fGv5TP6QexwedgAI5kcBo5g056nhACA4fy9ahKy7WMdYPRrVqZugPq7y60uvpB/Ib%2b8Dh93w/PUMh5fbhSDHBzCafKuwKVaIILGSIOQ5jurVmo4YLYbEgdSRTNu1FrRvHZsC38LNjWYZHgw8HNTRbZAbcTgcmGXnYzbRcpTDKcPNcGmYqYqlzGk9AenoTxRWATUE6PGXCjc/8iQgiCzobvfTQjHB6AwkfhLnwHCTwUYs1tIkVVVg92OvFN9I32RF%2b3yKB%2byd5uoyi0m1WYOY11%2btYtYB0Mh2ah4zzWgYsDMjOZsfkq1K2VR2DfLH1XN/3Maampkyt52W9vNlknb2BO8IvTmXlhKzNlYyYaup6L/XeUd2TMkAqDto/slgt%2b3OHjoF8uALChXghPVS/EPUv8W9XvU35uZ%2bN2bQI7JRS4%2bGibrL7i%2bhCkfgeNNRB3BdvAAO0T9uaGeyL1aXpz/c8jwOZm12qJ5kbVLPugoi/XyqVbUqb1O0nFVp3dAHTIW9oA9H5i50srvTLosFtornBCmnrIl5NnJ1XvzHsDPEyCdXpIcIxT9XdBzal0P2JLn2nbC2yHMtvmN5TA63zc5DzrgvCA1LXYlYYH8K5jEvn0qesa7%2br3EDXvSmgh61eXiZcOTyvZ6fvDyMhO9z897DezHjKRY/JZI1TIfm3zKyT1x2B9X9olI2HoGkED/beplz/qjYnNiUjo8xLWAJ7OHmK4/g%2bZJsDW/2fk3/wP%3C/diagram%3E%3Cdiagram%20id=%22yZX1ylmdUqg1LlmkzajN%22%20name=%22DB%22%3E7VrZdto6FP0aHpMlj%2bBHhjTpvUmbFZJS%2bnKXihXbjW1RIQLk6ytheR6YYux03QdY1rF0kPbZ2jrHpqMMvfU1gXP7DpvI7cjAIo7ZUUYdWZbYhxnm0EIpA%2b8xdt5CIxDWpWOiRaojxdilzjxtnGHfRzOaskFC8Crd7Rm7%2bWmMZ9BFOevEMakdWHsaiO03yLHs8IckIO54MOwsDAsbmniVMClXHWVIMKbBlbceIpcjE%2bIy/o7RbKn3bic3BtK/9e%2bN%2b/uLwNmnQ4ZESyDIp0e71mz/CfeV4T%2bP18tfT9rvm8nqKnT9Ct2lwEuslW5CAC2Cl3PRDRGK1kVRgj/D7mDPyUoRgoxXCHuIkg0bF3rXhZ9N0O6K5ioOoWYIm50MnyqMULDEilzH0LALgc4BSMm7kWJeGIlZY7CyHYrGczjjd1Zs1zCbTT32gyOJXT47rjvELias7WOfjygFOAlkeQjzQDaHlJJD6tb5SaDwnASMrZWmkYGuY/nsesbWjBg8A46Iw3ZzX9zwHNPkwwcELZw3QTvA2nPs%2bHS7FG3Q0Ubc15LiRSA/3PWCEvyC6oZ9nUF3kxa/ZFQKgiLXFRPQ1n3eTeOkgnNu9JcJ%2bGFhCt9Gn8EX4D48Tv/rX8h7YNXMTgfFUDYIVf74GNuYkYj9oA49jkXwzSxfiYnI4q%2bSgJJ4hF7knRJQFK33kAD0OPT16wvvm0fkyfppLBvSsLUSoIE0TpEwJoCKzv8Ur0FdUO2RFdWuAOUxrFSAMyOVz4qeFmzTyuAO%2biyz9vhyPuiWPyQAwouqXMpAlgxdl4CkG6qRInb3UlJZ4dENv5UczSWpJkEoVG%2bpm2e1yWon0cSE2tjCPnSvYuuAKYRvIlPAH/e5xUz3A8h/IUo3ou7j0UjHGq0d%2bp0Pv9REayqc8evROtnYhA2frTcxiDenoT/eiIdtW/E4s88rxjjyzPLJ4TBt75twYW/XIkWk4AiUUqKqOlvgJZmhin5iq1BILFTlTy2mGEEupM5renJFnNgOZcuGm0QHsU9iz/fcEDNXz%2bSrspIpJrP9lcr%2b7CKYQczOaCknELbXHsJKRxEW7CBsipC72NsAYQvDopxI2NNEzGiUE0kJi/hRzImDYpsgUPcgBrWFFCUHZb0qpmVSbgVUq1i2v7pD9dSeVtX/ZNWrQjyXYmVYvyMNzaVYM5fxTmRS8fG3Iyc6Jr03MidFL5/eR/lpMu%2bprWqVlI8iGZEKSCkJiM%2bUI/OeukVC2VMkSphzppNDbZIG0kE0aF04a8lc9w1n1SQTMjnA%2bOVkmaxLFtXs0yH5jLJYHr0UgA/o1UGr1kKo9RqEsFhStP9PlneTovK0co%2bTRW70ZNE/zskSlhl/Jw3OVZoCd8rwUZ4//54ifWkt/717eQgn2YanFdWP146tTA96FtcAJcrzhFML03xlqJdUOaGLYF5iVIZY7/BoLP9yp%2bR9W1sOb1XKlN4Fb33OfHjnILxGPkGtRTB6T9aa9Cf/pGJMIW0xgmrbOJgvYobYK3yJ1hYMta52NgxZM/63XaCc8R8Slas/%3C/diagram%3E%3Cdiagram%20name=%22API%22%20id=%226524lpE4w6_BnwlkG1Lg%22%3E7VzbcqM4EP2aPCaFJMD40XEys1M1U5sa7%2b5s9k02iq0JRh4h3/L1K0AyCLCd%2bAIOmYe4rKbVgdPqo%2b5GyRXqT1efOZ5NvjGfBFfQGnPqX6G7KwiB/JGCGR4TQxBrDOiLFlpKOqc%2biQxFwVgg6MwUjlgYkpEwZJhztjTVnlhQvo3BCAekJP1BfTFJpZ5jZfI/CB1P9C8ClroyxVpZCaIJ9tkyJ0L3V6jPGRPpt%2bmqT4IYGY0Loy%2brLw/jl8WvrjeYz4aPiyW%2bTo19esuUzSNwEorTmobq0cRa40V8CZ8aMi4mbMxCHNxn0lvO5qFPYquWHGU6XxmbSSGQwp9EiLVyPZ4LJkUTMQ3UVbKi4t94%2bo2jRo/G6G6lbCeDdW7wQDidEkG4loWCr3Om4uFj/lpmKhlpW%2blTx49aWCR7EFZ6EZvzEdmh56l1jfmYKHu99TeM8PU///3s/fUcrmxXXKMUfuWuz4TJR%2bNrOY%2bTAAu6MG8Oq3U/3uhlzpZflL/f4HuU2l3gYK5%2b04COw3hW/IFDX34qyXxWuU6%2b4qGkAsO3OIhnoLuRBDJ20%2b2CcEFlOPbUhSn1/XQZkYi%2b4GFiL/bJjNFQJM/o3F45dxsvxQbIqooa1OQsQvf6bwveyvq1dWNZlgqJdSpTIL3aI8r4Q/wwORX29BTJlVB02eYeDvei/TuCm4xg98gITqb2OMfrnIIKhfJyUgvVQZaxSPWe9em1%2bu5ufRuho/Rh19CXX9InPOnCd8r0RTAfTdrBVPZOppJEBTwTc72yL5ep3N9M1SRTdZpgKrfIJHuYqqiPQA1M0ikxyZ/cl36H1pCxZ50LuYFE93Yoxe5YJIsx1REcj55pOG4H72zZzzLeQbDAO/DSeccrubc/j4Q0y0sukyXeLP46nwa9kWB57ySefGARFZTFXhoyIW1UuE/EzJR3%2bFYnvY4CtjrDdc1dvaOGy6zM1fv%2bJFfh6lknrye6F8TvR7C7we0Z1TfE7sB5Jb1b1WulnlJS93Y%2bUi3Z3RmcspaENjiyetQUaxdC9nxcCUClc95hkvZOw9hpIkvb9GbVgtP14rYsrahvd/boe8fpI%2bScPwsEsMxhqqCsTgBVcjjFIR6TabxOWsFrYHfWYd3YHbNFdmThad62sul2amM81BbGM8tS8F4Yz2uC8VxkruEC452JYewKhkmm7aozRxMyek4AmcmFFrWEZNAeknE6XfuULFMDkVQ1JIPgvVeZwC7kBlbDZSY4pI94FEXDN5SWB7KxuaH4OJokA1ADUeuY3UvU4Njc9Di3l7t0fcWM84jwtvDivv4bdDwzUzpN9qWbejXQpHdA%2bI7mfLEJiJOlW%2bCgUN7X77/M4IVbWL6m4O2WgjcNzfgGFpQs2xK%2bW5LZXFPI9S49kYHlZt5XOuRYrYO8k2rIP1Cn0AsA5fwDgIoExDlXAqIfLIePztqfWOKjDCH315zpC9dRQk89qQCs2Sq7qDP9v6PkhdK3XEMhNStvM7Wc6jXhBlhIA0G3cTfAJjeSN1Ttxoaw2VWAsac03qCEr32NDLb0vY9MQBxQ3fLbmEhvTM06A%2bmVT8N9oqGfvNdV5XkbNqg0aHZvUHqzPs0JOG0ZmOW8jt4atrNDTsjVXi%2b%2bkQ4MTjGLx8thikZfScJyO0bXi7ots6Xftu1wwPsM%2bN0HyWTAA6twkuw0FeUm7grn02oI%2bIYPmsEDasxjwv9iAn7b5lJTwJcbRLrGHLFpnE63pMiEu3tEMqQR8tzK4LvgorN8SmswkaEXo%2bLiadzsTj%2blJDmdV3ZmDVWQ41xcMVrurPS%2bJHscX1AZ1hdQsduwRpC2n40yMPpOoorX9UFAZ1Ec1ssJFWQwwwkvLjkuvGvZ/CVYHPJPNAj6LIhf40gjyHeI59uxkuDsmeSueHCIXPecNbplAg8rXtXYThl3dC7c4QfBvQNvHDOFqjiLWSvy5eS3lcijQlcKVVBNrbi7HwN3u9CtgRXdwFpxL%2bd%2brcTdvTTcy1nbh8AdOQ3jXnHg%2bvP3h/55gCdAQt%2bpAr7rdhCuk%2bAbT2kqTvm0EvhyTrPBtDHoy6VOK6G3HRP4xpOaihee7QTeMhuhdtNkA8sFVDuBL/wlm30%2bqpHD7D%2b2pM2r7J/aoPv/AQ==%3C/diagram%3E%3C/mxfile%3E)

[برای نمایش ارتباطات روی من کلیک کنید](https://ibb.co/WxszynM)

