//
//  ChatMessageTableViewCell.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 04/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import UIKit

class ChatMessageTableViewCell: UITableViewCell {
    
    @IBOutlet weak var avatarImageView: UIImageView!
    @IBOutlet weak var messageContainerView: UIView!
    @IBOutlet weak var messageTextLabel: UILabel!
    
    var message: Message? {
        didSet {
            UIHelper.shared.downloadAndSetImage(imageView: avatarImageView, imageUrl: message!.author.avatarUrl)
            
            messageTextLabel.text = message!.text
        }
    }
    
    override func layoutSubviews() {
        super.layoutSubviews()
        messageContainerView.layer.cornerRadius = 13.0
        messageContainerView.layer.masksToBounds = true
    }
}
