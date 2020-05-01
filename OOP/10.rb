class Cs
  @@count = 0
  def initialize()
    @@count = @@count + 1
  end
  def Cs.getCount()
    return @@count
  end
end
i1 = Cs.new()
i2 = Cs.new()
i3 = Cs.new()
i4 = Cs.new()
p Cs.getCount()

# @ : instance에 들어감
# @@ : class에 들어감
# @가 없음 : method안에 들어감
