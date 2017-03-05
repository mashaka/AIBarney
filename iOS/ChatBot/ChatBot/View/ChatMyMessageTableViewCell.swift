//
//  ChatMyMessageTableViewCell.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 04/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import UIKit

class ChatMyMessageTableViewCell: UITableViewCell {
    @IBOutlet weak var messageContainerView: UIView!
    @IBOutlet weak var messageTextLabel: UILabel!
    @IBOutlet weak var activity: UIActivityIndicatorView!
    
    var message: Message? {
        didSet {
            messageTextLabel.text = message!.text
        }
    }
    
    var isSending: Bool = false {
        didSet {
            isSending ? activity.startAnimating() : activity.stopAnimating()
        }
    }
    
    override func layoutSubviews() {
        super.layoutSubviews()
        messageContainerView.layer.cornerRadius = 13.0
        messageContainerView.layer.masksToBounds = true
    }
}
