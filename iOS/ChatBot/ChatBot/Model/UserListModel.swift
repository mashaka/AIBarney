//
//  UserListModel.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 04/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import Foundation
import SwiftyJSON

struct UserListModel {
    var list: [User] = []
    
    mutating func setupWith(json: JSON) {
        list.removeAll()
        for userJson in json.arrayValue {
            let user = User(json: userJson)
            list.append(user)
        }
    }
    
    lazy var mockList: [User] = {
        return [
            User(id: "uid1", avatarUrl: URL(string: "empty"), firstname: "Alexey", lastname: "Zhuravlev"),
            User(id: "uid2", avatarUrl: URL(string: "empty"), firstname: "Mark", lastname: "Ryabov"),
            User(id: "uid3", avatarUrl: URL(string: "empty"), firstname: "Maria", lastname: "Sandrikova")
        ]
    }()
}
