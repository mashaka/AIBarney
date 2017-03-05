//
//  ChatTableViewCell.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 04/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import UIKit

class ChatTableViewCell: UITableViewCell {
    @IBOutlet weak var avatarImageView: UIImageView!
    @IBOutlet weak var fullNameLabel: UILabel!
    @IBOutlet weak var lastMessageText: UILabel!
    
    var chat: Chat? {
        didSet {
            fullNameLabel.text = chat!.partner.firstname + " " + chat!.partner.lastname
            UIHelper.shared.downloadAndSetImage(imageView: avatarImageView, imageUrl: chat?.partner.avatarUrl)
            
            if chat!.lastMessage != nil {
                lastMessageText.text = chat?.lastMessage?.text
            } else {
                lastMessageText.text = "no messages yet"
            }
        }
    }
}

