//
//  ChatListModel.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 04/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import Foundation

struct ChatListModel {
    var sections: [[Any]] = []
    
    mutating func loadModel() {
        sections = [createRecentChatsSection()]
    }
    
    func createRecentChatsSection() -> [Chat] {
        return []
    }
}
