//
//  ChoseUserTableViewCell.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 04/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import UIKit

class ChoseUserTableViewCell: UITableViewCell {
    
    @IBOutlet weak var avatarImageView: UIImageView!
    @IBOutlet weak var fullNameLabel: UILabel!
    
    var user: User? {
        didSet {
            fullNameLabel.text = user!.firstname + " " + user!.lastname
            UIHelper.shared.downloadAndSetImage(imageView: avatarImageView, imageUrl: user!.avatarUrl)
        }
    }
}
