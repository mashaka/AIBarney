//
//  ChatModel.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 04/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import Foundation
import SwiftyJSON
import PubNub

class Chat: NSObject, PNObjectEventListener {
    var partner: User
    var chatId: String
    
    var lastMessage: Message?
    var messages: [Message] = []
    
    var delegate: ChatVCProtocol?
    
    init(json: JSON, partner: User) {
        self.partner = partner
        self.chatId = json["id"].stringValue
        
        if !json["last_message"].isEmpty {
            self.lastMessage = Message(json: json["last_message"], author: partner)
        }
        
        super.init()
        pubnub()
        updateMessages()
    }
    
    func updateMessages() {
        API.getHistory(chatId: chatId, completion: updateMessagesCompletion)
    }
    
    func updateMessagesCompletion(json: JSON) {
        messages.removeAll()
        for jsonMessage in json.arrayValue {
            messages.append(Message(json: jsonMessage))
        }
    }
    
    // -------------------------
    
    func pubnub() {
        PubNubWrapper.shared.client.addListener(self)
        PubNubWrapper.shared.client.subscribeToChannels(["\(AuthData.shared.id!)_\(chatId)"], withPresence: false)
    }
    
    // -------------------------
    
    func client(_ client: PubNub, didReceiveMessage message: PNMessageResult) {
        let incomingMessage = Message(json: JSON(message.data.message!))
        messages.append(incomingMessage)
        delegate?.newIncomingMessage(at: messages.count - 1)
    }
}
