---
title: JWT Token 組成原理
parent: Others
---

# JWT Token 組成原理

（JSON Web Token）

Token是服務端生成的一串字串，以作客戶端進行請求的一個令牌。

當第一次登入後，伺服器生成一個Token便將此Token返回給客戶端，

以後客戶端只需帶上這個Token前來請求資料即可，無需再次帶上使用者名稱和密碼。

無狀態，符合restful原則，也適用於負載平衡。

每次APP請求的時候都驗證token和有效期。

比如隨機生成32位的字串作為token，儲存到伺服器中。

jwt詳細原理

https://iter01.com/586690.html

https://www.gushiciku.cn/pl/pSnF/zh-tw

## 邏輯

header.payload.Signature簽章

三者皆使用base64編碼加密

header ⇒ 含用什麼雜湊演算法(HS256)，得到Signature簽章值

```
{   
  "alg": "HS256", //雜湊演算法
  "typ": "JWT"   //token類型
}
```

payload ⇒ 含授權時間+有效期

```
{
  "user_id": 007,//認證使用者的資料
  "name": "Robin",//認證使用者的資料
    "exp":1300819380 //expiration time
}
```

簽章 ⇒ 將header和payload，以base64編碼後加上伺服器秘鑰，進行HS256雜湊運算

(運算完，再將結果用base64編碼)

```
//方法
HMACSHA256( base64UrlEncode(header) + "." +  base64UrlEncode(payload), secret)
```

## 儲存

客戶端儲存這token的全部資訊。(header.payload.Signature簽章)

服務端只需要儲存token的Signature簽章部分。(Signature簽章)

→ 為何要存? 因為就算token正確，也要驗證db中是否存有此token。

## 能用的演算法清單

```
  +--------------+-------------------------------+--------------------+
   | "alg" Param  | Digital Signature or MAC      | Implementation     |
   | Value        | Algorithm                     | Requirements       |
   +--------------+-------------------------------+--------------------+
   | HS256        | HMAC using SHA-256            | Required           |
   | HS384        | HMAC using SHA-384            | Optional           |
   | HS512        | HMAC using SHA-512            | Optional           |
   | RS256        | RSASSA-PKCS1-v1_5 using       | Recommended        |
   |              | SHA-256                       |                    |
   | RS384        | RSASSA-PKCS1-v1_5 using       | Optional           |
   |              | SHA-384                       |                    |
   | RS512        | RSASSA-PKCS1-v1_5 using       | Optional           |
   |              | SHA-512                       |                    |
   | ES256        | ECDSA using P-256 and SHA-256 | Recommended+       |
   | ES384        | ECDSA using P-384 and SHA-384 | Optional           |
   | ES512        | ECDSA using P-521 and SHA-512 | Optional           |
   | PS256        | RSASSA-PSS using SHA-256 and  | Optional           |
   |              | MGF1 with SHA-256             |                    |
   | PS384        | RSASSA-PSS using SHA-384 and  | Optional           |
   |              | MGF1 with SHA-384             |                    |
   | PS512        | RSASSA-PSS using SHA-512 and  | Optional           |
   |              | MGF1 with SHA-512             |                    |
   | none         | No digital signature or MAC   | Optional           |
   |              | performed                     |                    |
   +--------------+-------------------------------+--------------------+
```

