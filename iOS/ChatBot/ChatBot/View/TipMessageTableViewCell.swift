//
//  TipMessageTableViewCell.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 05/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import UIKit
import SwipeCellKit

class TipMessageTableViewCell: SwipeTableViewCell {
    
    @IBOutlet weak var messageContainerView: UIView!
    @IBOutlet weak var messageTextLabel: UILabel!
    
    var tip: Tip? {
        didSet {
            messageTextLabel.text = tip!.text
        }
    }
    
    override func layoutSubviews() {
        super.layoutSubviews()
        messageContainerView.layer.cornerRadius = 13.0
        messageContainerView.layer.masksToBounds = true
        
        messageContainerView.layer.borderColor = UIColor(white: 0.87, alpha: 1.0).cgColor
        messageContainerView.layer.borderWidth = 1.0
    }
    
}
