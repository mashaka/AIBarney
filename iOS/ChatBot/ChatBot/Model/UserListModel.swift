//
//  UserListModel.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 04/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import Foundation

struct UserListModel {
    var list: [User]
    
    lazy var mockList: [User] = {
        return [
            User(id: "uid1", avatarUrl: URL(string: "empty"), firstname: "Alexey", lastname: "Zhuravlev"),
            User(id: "uid2", avatarUrl: URL(string: "empty"), firstname: "Mark", lastname: "Ryabov"),
            User(id: "uid3", avatarUrl: URL(string: "empty"), firstname: "Maria", lastname: "Sandrikova")
        ]
    }()
}
