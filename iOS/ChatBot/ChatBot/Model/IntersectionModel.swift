//
//  IntersectionModel.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 05/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import Foundation
import SwiftyJSON

struct Intersection {
    
    var algoId: String
    var description: String
    var weight: String
    
    var tips: [Tip] = []

    init(json: JSON) {
        self.algoId = json["algo_id"].stringValue
        self.description = json["description"].stringValue
        self.weight = json["weight"].stringValue
        
        for tipJson in json["tips"].arrayValue {
            tips.append(Tip(json: tipJson))
        }
    }
}
