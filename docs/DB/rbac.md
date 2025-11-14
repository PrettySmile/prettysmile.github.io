---
title: RBAC
parent: DB
---

# RBAC
RBAC 就是：「設定角色 → 賦予權限 → 指派角色給使用者」。

= 角色為主，先給角色權限，再給人角色。

## RBAC 好處

- 📦 集中管理：角色變更不需修改使用者
- ✅ 易於維護與擴充
- 🧩 適合大型系統（多人、不同層級）

## 🛠️ 簡易流程（在程式中）

以 Node.js/NestJS 為例，常見的作法：

1. 定義角色 enum：
    
    ```tsx
    export enum Role {
      Admin = 'admin',
      Editor = 'editor',
      Viewer = 'viewer',
    }
    ```
    
2. 在使用者資料中加入角色：
    
    ```tsx
    @Entity()
    export class User {
      @Column({ type: 'enum', enum: Role })
      role: Role;
    }
    ```
    
3. 用 Guard 控制權限：
    
    ```tsx
    @UseGuards(RolesGuard)
    @Roles(Role.Admin)
    @Get('/users')
    findAllUsers() {
      return this.userService.findAll();
    }
    ```
    

## 🎯 RBAC 的 3 個核心概念

1. **使用者（User）**
    - 實際登入系統的帳號
2. **角色（Role）**
    - 一組權限（如 admin、editor）
3. **權限（Permission）**
    - 可以做哪些事情（像是 `createPost`, `deleteUser`）