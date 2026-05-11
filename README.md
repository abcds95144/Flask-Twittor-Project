# 專案名稱:Twittor - Flask 
：這是一個基於 Flask 開發的微型社群平台，核心在於實踐 RESTful API 設計與資料庫關聯建模。

## 技術規格 

後端 : Python / Flask / SQLAlchemy 

資料庫: MySQL 

前端 :

基礎: Jinja2 Template / Bootstrap 5 

動態: Vanilla JavaScript 

開發工具: Git / Postman (API 測試)

## ✨ 核心功能與技術亮點
使用者驗證系統：實作登入、註冊功能，並透過 werkzeug.security 進行密碼雜湊加密。

資料庫關聯設計：設計 User 與 Tweet 之間的 One-to-Many 關係，以及按讚與追蹤功能的 Many-to-Many 關係。

非同步按讚機制：為了讓按讚功能更流暢，我嘗試用 Vanilla JS (Fetch API) 來做，這樣使用者按讚時頁面就不會整頁重整（原本整頁重整的體驗很卡）。

## 📈 未來演進規劃 
Phase 1 (進行中)：目前使用 Bootstrap 完善介面，並優化後端 API 錯誤處理。

Phase 2 (計畫)：

將前端重構成 Vue.js，達成前後端完全分離。

導入 JWT (JSON Web Token) 驗證機制。

Phase 3：部署至 AWS EC2，並加入 Redis 作為熱門貼文的快取層。

## ⚙️ 如何在本地執行
git clone []

建立虛擬環境：python -m venv venv

啟動環境：venv\Scripts\activate (Windows)

安裝依賴：pip install -r requirements.txt

啟動專案：flask run
