$response = Invoke-RestMethod -Uri "https://api.steampowered.com/IGameServersService/GetServerList/v1/?filter=\appid\107410\addr\135.125.140.176&key=A67FA2E66CF66B5C4AAA583F6253636A" -Headers @{
"method"="GET"
  "authority"="api.steampowered.com"
  "scheme"="https"
  "path"="/IGameServersService/GetServerList/v1/?filter=\appid\107410\addr\135.125.140.176&key=A67FA2E66CF66B5C4AAA583F6253636A"
  "upgrade-insecure-requests"="1"
  "user-agent"="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36"
  "accept"="text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
  "sec-gpc"="1"
  "sec-fetch-site"="none"
  "sec-fetch-mode"="navigate"
  "sec-fetch-user"="?1"
  "sec-fetch-dest"="document"
  "accept-encoding"="gzip, deflate, br"
  "accept-language"="en-GB,en-US;q=0.9,en;q=0.8"
  "cookie"="dp_user_sessionid=7324aac9277c853bde17ab2859141485; dp_user_language=1"
} | ConvertTo-Json | Out-File -Encoding utf8 "./PS-Response/response.json"