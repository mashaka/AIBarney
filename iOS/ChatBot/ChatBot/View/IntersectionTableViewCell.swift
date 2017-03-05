//
//  IntersectionTableViewCell.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 05/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import UIKit

class IntersectionTableViewCell: UITableViewCell {
    @IBOutlet weak var intersectionNameLabel: UILabel!
    
    var intersection: Intersection? {
        didSet {
            intersectionNameLabel.text = intersection!.description
        }
    }
}
