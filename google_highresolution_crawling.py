import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
from selenium.webdriver.common.by import By


# 검색어 여러개로 할 때는 해당 주석을 풀어주세요
# searcharr = ['coronavirus en japan',
#             'मास्क पहन कर', 'बिना मास्क', 'सड़क का मुखौटा', 'स्कूल का मुखौटा']# 이건 나중에 6월 24일에 할 것
# for search in searcharr:

  
# 2022 07 05 이후 검색어  
# 감염, costume party, religious veil, fun, leisure


# search 바꾸세요!
searchs = ['event3', 'fun2', 'mask airport europe', 'demonstration', 'fun3', 
          
          'coronavirus images of people', 'masque', 'leisure2', 'fun4', 'tokyo coronavirus'
          
          'news conference', '한국 코로나 마스크', 'people wearing masks in 2009', 'do you have to wear a mask', 'Coronavirus disease 2019', 
          
          'event4', '路上 戴 口罩', 'covid 19 pictures around the world', 'standing3', 'origen del covid 19 en wuhan',
          
          '감염2', 'leisure3', 'fun4', 'costume party1', 'costume party2'
          ]

links = ['https://www.google.com/search?hl=ko&tbs=simg:CAESgQIJu1seLuneUTEa9QELEKjU2AQaAghCDAsQsIynCBo6CjgIBBIU8C3aEb0jnxGTIrsF_1jW0FLI8ghgaGiiFfeSNQj7qGLu-BYgTS4Pvz-upA-4-31riIAUwBAwLEI6u_1ggaCgoICAESBBXl31IMCxCd7cEJGooBChgKBWV2ZW502qWI9gMLCgkvbS8wODFwa2oKGwoIY3VzdG9tZXLapYj2AwsKCS9tLzAxajBtawoXCgNmdW7apYj2AwwKCi9tLzBkczk5bGgKGQoHbGVpc3VyZdqliPYDCgoIL20vMDRnM3IKHQoKc21hcnRwaG9uZdqliPYDCwoJL20vMDE2OXpoDA&q=event&tbm=isch&sa=X&ved=2ahUKEwingK6EguP4AhW1nFYBHfHbAnMQjJkEegQIChAC&biw=1278&bih=1311&dpr=1',
         'https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAESiQIJt6VuZeS4QZka_1QELEKjU2AQaAghDDAsQsIynCBo6CjgIBBIUiDnaEdclnxG9I4IYsjyeJZMimSIaGkXSqkxVv6IhoUTSWFku1kqOCqyIRwZviO7iIAUwBAwLEI6u_1ggaCgoICAESBGTzfTEMCxCd7cEJGpIBChcKA2Z1btqliPYDDAoKL20vMGRzOTlsaAobCghzbmFwc2hvdNqliPYDCwoJL20vMDZwZzIyCiEKDmZhbiBjb252ZW50aW9u2qWI9gMLCgkvbS8wMnhobXMKGQoHbGVpc3VyZdqliPYDCgoIL20vMDRnM3IKHAoJcGFzc2VuZ2Vy2qWI9gMLCgkvbS8wY2IweG0M&q=fun&tbm=isch&ved=2ahUKEwivzKnTguP4AhVHmVYBHeLvC3MQjJkEegQIERAC&biw=1278&bih=1311&dpr=1',
         'https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAESkgIJZjxnqPIQH2AahgILEKjU2AQaAghCDAsQsIynCBo6CjgIBBIUnxHaEbI81yW9I4IYxiHNNpMisBQaGoc8md0I2zNDcUCx3mgh1VMeuYOx3z78tvVCIAUwBAwLEI6u_1ggaCgoICAESBM95rnsMCxCd7cEJGpsBChwKCXBhc3NlbmdlctqliPYDCwoJL20vMGNiMHhtChsKCGNoZWNrLWlu2qWI9gMLCgkvbS8wOHo4am4KGwoIY3VzdG9tZXLapYj2AwsKCS9tLzAxajBtawoeCgtjbGVhbmxpbmVzc9qliPYDCwoJL20vMDIwczRwCiEKCnF1ZXVlIGFyZWHapYj2Aw8KDS9nLzExYmM1OWRqejUM&q=mask+airport+europe&tbm=isch&ved=2ahUKEwiOjtrrguP4AhVm2jgGHREcCh4QjJkEegQIHBAC&biw=1278&bih=1311&dpr=1',
         'https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAES3QEJYZKvCzlvXR8a0QELELCMpwgaOgo4CAQSE_1AtiDmQIsITLoowpyOyMMYExRwaGzD5SP2njSy3Bn9zp3aruWBrlH6mdiNpIkaBRSAFMAQMCxCOrv4IGgoKCAgBEgQog6f9DAsQne3BCRpyCiAKDWRlbW9uc3RyYXRpb27apYj2AwsKCS9tLzBnbnd6NAoXCgNmdW7apYj2AwwKCi9tLzBkczk5bGgKGAoFY3Jvd2TapYj2AwsKCS9tLzAzcXR3ZAobCghhdWRpZW5jZdqliPYDCwoJL20vMDMzbHByDA&q=demonstration&tbm=isch&ved=2ahUKEwjk97j-guP4AhVNklYBHYlcAnMQjJkEegQIDRAC&biw=1278&bih=1311&dpr=1',
         'https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAES9wEJQod34YBqYjsa6wELEKjU2AQaAghCDAsQsIynCBo6CjgIBBIUsjz_1JpYe8C2_1Fpk22QiQIqwtsjAaGqc8JlmhPtbwqV_1OpA1kf5fwsfmIBsKag_1B_1IAUwBAwLEI6u_1ggaCgoICAESBNTZkGkMCxCd7cEJGoABChcKA2Z1btqliPYDDAoKL20vMGRzOTlsaAoYCgZtYXNxdWXapYj2AwoKCC9tLzBqeXQ2ChcKBG1hc2vapYj2AwsKCS9tLzAxa3I0MQoaCgdjb3NwbGF52qWI9gMLCgkvbS8wMTRodDMKFgoEdHJlZdqliPYDCgoIL20vMDdqN3IM&q=fun&tbm=isch&ved=2ahUKEwjRlrGUg-P4AhUDC94KHcQRCSAQjJkEegQIIxAC&biw=1278&bih=1311&dpr=1',
         
         'https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAESlAIJCIVhW85Oh7oaiAILEKjU2AQaAghCDAsQsIynCBo6CjgIBBIUkCLwLaYMsjzcLog5whP_1JskSvxYaGqU7qPTJ3rGA-U69n8xtVqKqP2rjZpC-Q3w2IAUwBAwLEI6u_1ggaCgoICAESBBGVUqgMCxCd7cEJGp0BCh8KDHNvY2lhbCBncm91cNqliPYDCwoJL20vMDFiNHE5CiAKDWNvc3R1bWUgcGFydHnapYj2AwsKCS9tLzA0dnFjMwoXCgNmdW7apYj2AwwKCi9tLzBkczk5bGgKJwoUYWNhZGVtaWMgaW5zdGl0dXRpb27apYj2AwsKCS9tLzA2YmRwawoWCgRjaXR52qWI9gMKCggvbS8wMW4zMgw&q=coronavirus+images+of+people&tbm=isch&ved=2ahUKEwiR4sm5g-P4AhX_klYBHdubBnIQjJkEegQIBxAC&biw=1278&bih=1311&dpr=1',
         'https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAESigIJzOv8Px-Hiuga_1gELEKjU2AQaAghDDAsQsIynCBo7CjkIBBIU8C3CE5Ailh7aEccj8hCyMKYMoxkaG60f8MRhuXI5DFa_1fhv1-c3u2FKVIVuGEAFqhyAFMAQMCxCOrv4IGgoKCAgBEgTqdqriDAsQne3BCRqSAQoYCgZtYXNxdWXapYj2AwoKCC9tLzBqeXQ2ChcKA2Z1btqliPYDDAoKL20vMGRzOTlsaAogCg1zdXJnaWNhbCBtYXNr2qWI9gMLCgkvbS8wM2YwcmYKGQoGc3RyZWV02qWI9gMLCgkvbS8wMWM4YnIKIAoNY29zdHVtZSBwYXJ0edqliPYDCwoJL20vMDR2cWMzDA&q=masque&tbm=isch&ved=2ahUKEwjKs7X8g-P4AhWJqFYBHRB3CXMQjJkEegQIGxAC&biw=1278&bih=1311&dpr=1',
         'https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAES9gEJUtSSsWrkiika6gELEKjU2AQaAghCDAsQsIynCBo5CjcIBBIT8C2mDNoRLqwtkCKyPJIUsjDyEBoarLNZ_1ovzI0C8ofc8iL-H0Ah4c4FTi288seUgBTAEDAsQjq7-CBoKCggIARIEChmPaQwLEJ3twQkagAEKGQoHbGVpc3VyZdqliPYDCgoIL20vMDRnM3IKGAoFZXZlbnTapYj2AwsKCS9tLzA4MXBragoXCgNmdW7apYj2AwwKCi9tLzBkczk5bGgKFgoEY2l0edqliPYDCgoIL20vMDFuMzIKGAoFY3Jvd2TapYj2AwsKCS9tLzAzcXR3ZAw&q=leisure&tbm=isch&ved=2ahUKEwj3nJSFiOP4AhUbUd4KHW0fCIAQjJkEegQICBAC&biw=1278&bih=1311&dpr=1'
         'https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAESsAEJ8jGOr-7OM_1EapAELEKjU2AQaAghDDAsQsIynCBo7CjkIBBIUxgSQIvAtlh7yEIow-weeLsITvSgaG3dCpfaR5Gh4OjZR1FtzeNTBYzWulJ76VPkJGyAFMAQMCxCOrv4IGgoKCAgBEgSEJ3hNDAsQne3BCRo5ChcKA2Z1btqliPYDDAoKL20vMGRzOTlsaAoeCgxtb2JpbGUgcGhvbmXapYj2AwoKCC9tLzA1MGs4DA&q=fun&tbm=isch&ved=2ahUKEwjsvMOyiOP4AhU_tlYBHbtwBXMQjJkEegQIERAC&biw=1278&bih=1311&dpr=1',
         'https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAESkAIJI9RUStkprwwahAILEKjU2AQaBAhCCEMMCxCwjKcIGjoKOAgEEhO_1FrIwkCIu8C2SCPEKsjzYCLkFGhtzAEJldquQyav_1hIkE9Ovf4LE9-MssJfjzjjYgBTAEDAsQjq7-CBoKCggIARIEtshT5wwLEJ3twQkalwEKHwoMc29jaWFsIGdyb3Vw2qWI9gMLCgkvbS8wMWI0cTkKGAoFZXZlbnTapYj2AwsKCS9tLzA4MXBragokChBzZWNvbmRhcnkgc2Nob29s2qWI9gMMCgovbS8wMjV0amNiChoKB3N0dWRlbnTapYj2AwsKCS9tLzAxNGNuYwoYCgVjcm93ZNqliPYDCwoJL20vMDNxdHdkDA&q=tokyo+coronavirus&tbm=isch&ved=2ahUKEwiTiM3oiOP4AhVNp1YBHWXCCHAQjJkEegQIBxAC&biw=1278&bih=1311&dpr=1',
         
         'https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAESnQIJoA9ATnJiqAkakQILEKjU2AQaBAhCCEMMCxCwjKcIGjkKNwgEEhPXJdoRsjzGIZ8RniXlIJMiAIMmGhqBReXbyQfhuZa00ApVv1idEiLFpqx4vYMm1CAFMAQMCxCOrv4IGgoKCAgBEgT67PQxDAsQne3BCRqlAQoiCg9uZXdzIGNvbmZlcmVuY2XapYj2AwsKCS9tLzAxczhmeAohCg10diBqb3VybmFsaXN02qWI9gMMCgovbS8wMnhocjJqCiIKDm1lZGljYWwgc3VwcGx52qWI9gMMCgovbS8waDhscnYwCh8KDHNwb2tlc3BlcnNvbtqliPYDCwoJL20vMDF4cjY2ChcKA2Z1btqliPYDDAoKL20vMGRzOTlsaAw&q=news+conference&tbm=isch&ved=2ahUKEwjthZPbiuP4AhVUft4KHf6RDOUQjJkEegQIHhAC&biw=1278&bih=1311&dpr=1',
         'https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAESiQIJ4u12gq6pv60a_1QELEKjU2AQaBAhCCEMMCxCwjKcIGjkKNwgEEhPwLZAisjyIOS7CE9scjCrNNtoRGhpt5GwT5oci7z2l7jcGznjaCuldfU7H8auiSSAFMAQMCxCOrv4IGgoKCAgBEgRenCvaDAsQne3BCRqRAQogCg1jb3N0dW1lIHBhcnR52qWI9gMLCgkvbS8wNHZxYzMKFwoDZnVu2qWI9gMMCgovbS8wZHM5OWxoCiAKDXN1cmdpY2FsIG1hc2vapYj2AwsKCS9tLzAzZjByZgoYCgVzY2FyZtqliPYDCwoJL20vMDJoMTlyChgKBWNyb3dk2qWI9gMLCgkvbS8wM3F0d2QM&q=%ED%95%9C%EA%B5%AD+%EC%BD%94%EB%A1%9C%EB%82%98+%EB%A7%88%EC%8A%A4%ED%81%AC&tbm=isch&ved=2ahUKEwiwuMeHi-P4AhWlplYBHSvJDcEQjJkEegQIBRAC&biw=1278&bih=1311&dpr=1',
         'https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAEShAIJ6-DroVrHDa8a-AELEKjU2AQaAghCDAsQsIynCBo6CjgIBBIUgj2yPNkI4S-sLYQ4xiGIOacKoSIaGgMHnQUTLZaop0FmS50zR9iuGcRXXUNoCcDlIAUwBAwLEI6u_1ggaCgoICAESBL3IKtIMCxCd7cEJGo0BCiAKDWRlbW9uc3RyYXRpb27apYj2AwsKCS9tLzBnbnd6NAoXCgNmdW7apYj2AwwKCi9tLzBkczk5bGgKHAoIYWN0aXZpc3TapYj2AwwKCi9tLzBqXzd2bDYKGgoHcHJvdGVzdNqliPYDCwoJL20vMDFuZF9uChYKBHRyZWXapYj2AwoKCC9tLzA3ajdyDA&q=people+wearing+masks+in+2009&tbm=isch&ved=2ahUKEwilyNi2i-P4AhVRmlYBHYgUCXMQjJkEegQIHhAC&biw=1278&bih=1311&dpr=1',
         'https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAESjAIJLKkRaxvhDmgagAILEKjU2AQaAghCDAsQsIynCBo7CjkIBBIUuT_1hL9oRxC6yPL4euQ3HKrQGgBUaGxhVNz5ZeTaaof444dY7MJ5VDTNtG5oaPmBYeiAFMAQMCxCOrv4IGgoKCAgBEgSncHyvDAsQne3BCRqUAQohCg56ZWJyYSBjcm9zc2luZ9qliPYDCwoJL20vMDE0djdwChkKBnN0cmVldNqliPYDCwoJL20vMDFjOGJyChoKCHNpZGV3YWxr2qWI9gMKCggvbS8wZG5oeQoZCgd3YWxraW5n2qWI9gMKCggvbS8wODNtZwodCgpwZWRlc3RyaWFu2qWI9gMLCgkvbS8wMTdyOHAM&q=do+you+have+to+wear+a+mask&tbm=isch&ved=2ahUKEwie_fThi-P4AhXotlYBHa87B3MQjJkEegQIDBAC&biw=1278&bih=1311&dpr=1'
         'https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAEShwIJ_19a3I-W87rYa-wELEKjU2AQaBAhCCEMMCxCwjKcIGjsKOQgEEhTaEbI84x3DA9clsjCmDOUgyQ6AHxobRfFbJIaW-aQph2IKxpycRvaOVrVl1Hrcrh-NIAUwBAwLEI6u_1ggaCgoICAESBFSJtwUMCxCd7cEJGo0BChwKCHN0YW5kaW5n2qWI9gMMCgovbS8wMnd6Ym1qChgKBWV2ZW502qWI9gMLCgkvbS8wODFwa2oKGQoHbGVpc3VyZdqliPYDCgoIL20vMDRnM3IKHQoKdXJiYW4gYXJlYdqliPYDCwoJL20vMDM5amJxChkKBnN0cmVldNqliPYDCwoJL20vMDFjOGJyDA&q=Coronavirus+disease+2019&tbm=isch&ved=2ahUKEwikg4OEjOP4AhVOA4gKHY7ICaQQjJkEegQIDRAC&biw=1278&bih=1311&dpr=1',
         
         'https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAES_1wEJ2baghY7QJwUa8wELEKjU2AQaBAhCCEMMCxCwjKcIGjoKOAgEEhTwLaYM2hHHI7Iw3C7CE5IU5TLyEBoac-VX_1FvwuxFLJPXjF406Mz8nUqJChw-o1EEgBTAEDAsQjq7-CBoKCggIARIEeC73MAwLEJ3twQkahgEKGAoFZXZlbnTapYj2AwsKCS9tLzA4MXBragoXCgNmdW7apYj2AwwKCi9tLzBkczk5bGgKGQoHbGVpc3VyZdqliPYDCgoIL20vMDRnM3IKGQoGc3RyZWV02qWI9gMLCgkvbS8wMWM4YnIKGwoIc25hcHNob3TapYj2AwsKCS9tLzA2cGcyMgw&q=event&tbm=isch&ved=2ahUKEwilu4-VjOP4AhWXZt4KHYknBMYQjJkEegQIEBAC&biw=1278&bih=1311&dpr=1',
         'https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAES8wEJttK4KrC_1fKAa5wELELCMpwgaOwo5CAQSFNoRsjzwLbkNuT_1-Jfgm1yX0FMcjGhtzcJXwnqQFfpCSYKf8albOKT504j1kD0AkIi0gBTAEDAsQjq7-CBoKCggIARIEaKNvggwLEJ3twQkahgEKGwoIc25hcHNob3TapYj2AwsKCS9tLzA2cGcyMgoYCgVldmVudNqliPYDCwoJL20vMDgxcGtqChcKA2Z1btqliPYDDAoKL20vMGRzOTlsaAoZCgdsZWlzdXJl2qWI9gMKCggvbS8wNGczcgoZCgZzdHJlZXTapYj2AwsKCS9tLzAxYzhicgw&q=%E8%B7%AF%E4%B8%8A+%E6%88%B4+%E5%8F%A3%E7%BD%A9&tbm=isch&ved=2ahUKEwiJjPTnjOP4AhUW_GEKHUNFCC8QjJkEegQIDhAC&biw=1278&bih=1311&dpr=1',
         'https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAES8QEJXpI6NB_108qca5QELELCMpwgaOQo3CAQSE9oRsjzwLUS6AuMdiDnCNrk_11yUaGg3R6-Lw6oSbg6Hmt8SfBFd7ZAtosD3A-G1AIAUwBAwLEI6u_1ggaCgoICAESBNtYpjwMCxCd7cEJGoYBChsKCHNuYXBzaG902qWI9gMLCgkvbS8wNnBnMjIKFwoDZnVu2qWI9gMMCgovbS8wZHM5OWxoChgKBWV2ZW502qWI9gMLCgkvbS8wODFwa2oKGQoGZHVzdGVy2qWI9gMLCgkvbS8wNmgxeDQKGQoHbGVpc3VyZdqliPYDCgoIL20vMDRnM3IM&q=covid+19+pictures+around+the+world&tbm=isch&ved=2ahUKEwjZoauCjeP4AhX6UvUHHYVbBFsQjJkEegQICRAC&biw=1278&bih=1311&dpr=1',
         'https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAESjwIJmkAQMqnkp-wagwILEKjU2AQaBAhCCEMMCxCwjKcIGjoKOAgEEhMu8C2GDOUrvSOfEZAi1SKyPII0Ght3sIIBymkZBqVP3XIEChggQpOtPAJPeQ5qoHwgBTAEDAsQjq7-CBoKCggIARIEgPlW7QwLEJ3twQkalgEKHAoIc3RhbmRpbmfapYj2AwwKCi9tLzAyd3pibWoKHAoJZ2VudGxlbWFu2qWI9gMLCgkvbS8wMTlwNXEKGAoFZXZlbnTapYj2AwsKCS9tLzA4MXBragomChN3aGl0ZS1jb2xsYXIgd29ya2Vy2qWI9gMLCgkvbS8wMWtxM3gKFgoEaGFsbNqliPYDCgoIL20vMGQ0dm4M&q=standing&tbm=isch&ved=2ahUKEwiLyOiVjeP4AhV2mVYBHcLEB3IQjJkEegQIKBAC&biw=1278&bih=1311&dpr=1',
         'https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAESjQIJJegG5kcss6MagQILEKjU2AQaAghCDAsQsIynCBo7CjkIBBIUrC3cLog5sjzJEsYhlh7XJfAt2QgaG3Ywy62Aw72rX9Wz55bUatmXtK1mIJTZs91AKiAFMAQMCxCOrv4IGgoKCAgBEgTOyk8ODAsQne3BCRqVAQofCgxzb2NpYWwgZ3JvdXDapYj2AwsKCS9tLzAxYjRxOQogCg1kZW1vbnN0cmF0aW9u2qWI9gMLCgkvbS8wZ253ejQKGQoHbGVpc3VyZdqliPYDCgoIL20vMDRnM3IKFwoDZnVu2qWI9gMMCgovbS8wZHM5OWxoChwKCGFjdGl2aXN02qWI9gMMCgovbS8wal83dmw2DA&q=origen+del+covid+19+en+wuhan&tbm=isch&ved=2ahUKEwiTvLawjeP4AhVeUPUHHWh3CT0QjJkEegQIDhAC&biw=1278&bih=1311&dpr=1',
         
         'https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAEShwIJvoF8x3nvoVca-wELELCMpwgaOgo4CAQSFNoRxyPwLf4lsjz0FLIw-STaDNkzGhoYY3d33h3RYPhuCtqtmlSJYhyTvtxbkY9hliAFMAQMCxCOrv4IGgoKCAgBEgTnmPZ3DAsQne3BCRqbAQohCg5oeWJyaWQgYmljeWNsZdqliPYDCwoJL20vMDNwMmg5ChsKCHNuYXBzaG902qWI9gMLCgkvbS8wNnBnMjIKIgoOYmljeWNsZSBiYXNrZXTapYj2AwwKCi9tLzAycWQzeXoKGQoGc3RyZWV02qWI9gMLCgkvbS8wMWM4YnIKGgoIc2lkZXdhbGvapYj2AwoKCC9tLzBkbmh5DA&q=%EA%B0%90%EC%97%BC&tbm=isch&ved=2ahUKEwivhIqOjuP4AhXYc94KHR0fB_sQjJkEegQIBxAC&biw=1278&bih=1311&dpr=1',
         'https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAES_1AEJt_1DIpdCDbUUa8AELELCMpwgaOgo4CAQSFNoR8C2yMLI8sBSmDMcjkhTlIJ05Ghp4VOrRN8s1VuFK2Wh4DLmdXsQ4HWArz-ApAyAFMAQMCxCOrv4IGgoKCAgBEgR5_1E0EDAsQne3BCRqQAQoZCgdsZWlzdXJl2qWI9gMKCggvbS8wNGczcgoYCgVldmVudNqliPYDCwoJL20vMDgxcGtqCh8KDGNvbnZlcnNhdGlvbtqliPYDCwoJL20vMDFoOG4wChkKBnN0cmVldNqliPYDCwoJL20vMDFjOGJyCh0KCHBhcmEtc29s2qWI9gMNCgsvZy8xMjJmajk2Yww&q=leisure&tbm=isch&ved=2ahUKEwiumqqfjuP4AhVpm1YBHSAbCHMQjJkEegQIGRAC&biw=1278&bih=1311&dpr=1'
         'https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAESgQIJWL6bj_18cYXUa9QELEKjU2AQaAghDDAsQsIynCBo6CjgIBBIT8C3yEMITkCKWHqwtniXeLcUcABobpny_1fjsKxYvtCoRG3a15uIxJzXV42vvCI6B8IAUwBAwLEI6u_1ggaCgoICAESBHOM2LUMCxCd7cEJGooBChcKA2Z1btqliPYDDAoKL20vMGRzOTlsaAoaCghmZXN0aXZhbNqliPYDCgoIL20vMGhyNWsKGQoHbGVpc3VyZdqliPYDCgoIL20vMDRnM3IKHgoLY2VsZWJyYXRpbmfapYj2AwsKCS9qLzZja3F0cAoYCgVjcm93ZNqliPYDCwoJL20vMDNxdHdkDA&q=fun&tbm=isch&ved=2ahUKEwje38OakOP4AhXS_WEKHdAKBogQjJkEegQICBAC&biw=1278&bih=1311&dpr=1'
         'https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAESiAIJwGQPizJ3fpoa_1AELEKjU2AQaAghCDAsQsIynCBo6CjgIBBIUxgTwLZ4uwhOmJZYekCLyENYn2AgaGqv3PNfvfiraZu3qt-qPlmBbQ1Qax7uHj56cIAUwBAwLEI6u_1ggaCgoICAESBI1W1IAMCxCd7cEJGpEBCiAKDWNvc3R1bWUgcGFydHnapYj2AwsKCS9tLzA0dnFjMwocCglmb3IgYWR1bHTapYj2AwsKCS9hLzkzY3dfeQoXCgNmdW7apYj2AwwKCi9tLzBkczk5bGgKGQoHbGVpc3VyZdqliPYDCgoIL20vMDRnM3IKGwoIZm9yIHRlZW7apYj2AwsKCS9hLzZxMzA2Nww&q=costume+party&tbm=isch&ved=2ahUKEwjQup7gkOP4AhWKmFYBHRizCHMQjJkEegQIDhAC&biw=1278&bih=1311&dpr=1'
         'https://www.google.com/search?sa=G&hl=ko&tbs=simg:CAESggIJot62FKdnrRAa9gELELCMpwgaOwo5CAQSFPAt_1yaWHrI8mTa_1FsYEuj2mJZAiGhtrt4HpHZQpr0M0DSZuo_1Vd0lzLwecVnplizRsgBTAEDAsQjq7-CBoKCggIARIEzavAlgwLEJ3twQkalQEKIAoNY29zdHVtZSBwYXJ0edqliPYDCwoJL20vMDR2cWMzChcKA2Z1btqliPYDDAoKL20vMGRzOTlsaAoXCgRtYXNr2qWI9gMLCgkvbS8wMWtyNDEKGgoHY29zcGxhedqliPYDCwoJL20vMDE0aHQzCiMKEWhhbGxvd2VlbiBjb3N0dW1l2qWI9gMKCggvbS8wcHRzcAw&q=costume+party&tbm=isch&ved=2ahUKEwiyguOHkeP4AhWtqFYBHUQcDnEQjJkEegQIIxAC&biw=1278&bih=1311&dpr=1'
         ]


for i in range(len(searchs)):

    search = searchs[i]
    driver = webdriver.Chrome('chromedriver.exe')

    driver.get(links[i])
    # elem = driver.find_element("name","q")
    # elem.send_keys(search)
    # elem.send_keys(Keys.RETURN)

    # 이렇게 하면 검색어 안치고도 들어갈 수 있습니다.
    # driver.get()
    # 검색어 바꿔줘야 합니다.

    SCROLL_PAUSE_TIME = 3
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    SAVE_FLAG = False
    def timeout(limit_time): #timeout
        start = time.time()
        while True:
            if time.time() - start > limit_time or SAVE_FLAG:
                raise Exception('timeout. or image saved.')

    while True: #검색 결과들을 스크롤해서 미리 로딩해둠.
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element(".mye4qd").click()
            except:
                break
        last_height = new_height

    # images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
    count = 0
    for image in images:
        SAVE_FLAG = False
        timer = threading.Thread(target=timeout, args=(30,))
        try:
            image.click()
            time.sleep(4)
            # timer.start()
            #이미지의 XPath 를 붙여넣기 해준다. >> F12 를 눌러서 페이지 소스의 Element에서 찾아보면됨.
            # imgUrl = driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img').get_attribute("src")
            imgUrl = driver.find_element(By.XPATH, '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img').get_attribute("src")
            urllib.request.urlretrieve(imgUrl, "test/"+ search + "_{0:04}".format(count) + ".jpg") #저장할 이미지의 경로 지정
            print('Save images : ', "test/"+ search + "_{0:04}".format(count) + ".jpg")
            print(f'{search} are processing')
            SAVE_FLAG = True
            count += 1
        # if timer.is_alive():
            #     timer.join()
        except Exception as e:
            print('passed')
            continue
            # if timer.is_alive():
            #     timer.join()
            # else:
            #     continue

    print('driver end. Total images : ', count)
    driver.close()