//
//  CategoryCollectionViewCell.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 05/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import UIKit

class CategoryCollectionViewCell {
    @IBOutlet weak var categoryCoverImageView: UIImageView!
    @IBOutlet weak var categoryNameLabel: UILabel!
    
    var category: Category? {
        didSet {
            categoryCoverImageView.image = category!.categoryType.image()
            categoryNameLabel.text = category!.categoryType.name()
        }
    }
}
