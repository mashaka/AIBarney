//
//  TipModel.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 05/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import Foundation
import SwiftyJSON

struct Tip {
    
    var algoId: String
    var text: String
    var weight: String
    
    init(json: JSON) {
        self.algoId = json["algo_id"].stringValue
        self.text = json["text"].stringValue
        self.weight = json["weight"].stringValue
    }
    
}
