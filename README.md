# Twittor - Flask 社群平台實作

這是一個基於 Flask 開發的微型社群平台，核心在於實踐登入、註冊、追蹤、貼文、按讚功能與資料庫關聯建模。

## 🛠 技術規格

* **後端**: Python / Flask / SQLAlchemy
* **資料庫**: MySQL
* **前端**: 
    * **基礎**: Jinja2 Template / Bootstrap 5
    * **動態**: Vanilla JavaScript (Fetch API / RESTful API)
* **開發工具**: Git / Postman

## ✨ 核心功能與技術亮點

* **使用者驗證系統**：實作登入、註冊功能，並透過 `werkzeug.security` 進行**密碼雜湊加密**；針對重置密碼功能導入**JWT**確保驗證連結的時效性與安全性。
* **資料庫關聯設計**：設計 **User與Tweet的一對多** 關係，以及按讚與追蹤功能的**多對多**關係。
* **非同步操作**：為了優化使用者體驗，結合 **RESTful API**與**Vanilla JS (Fetch API)** 實作按讚功能，達成無需重新整理頁面的流暢互動。

## 📈 未來演進規劃

* **Phase 1 (進行中)**：使用 Bootstrap 5 完善介面 UI/UX，並強化後端 API 的異常處理邏輯。
* **Phase 2 (計畫)**：將前端重構成 **Vue.js**，達成前後端完全分離與標準 RESTful 架構。
* **Phase 3**：部署至**AWS EC2**，並加入 **Redis**作為熱門貼文的快取層以提升效能。

## ⚙️ 如何在本地執行

1. **複製儲存庫**: `git clone [https://github.com/abcds95144/test.git]`
2. **建立虛擬環境**: `python -m venv venv`
3. **啟動環境**: `venv\Scripts\activate` (Windows)
4. **安裝依賴**: `pip install -r requirements.txt`
5. **啟動專案**: `flask run`****

安裝依賴：pip install -r requirements.txt

啟動專案：flask run
